from logical_expression.LogicalExpression import LogicalExpression


class CalculationMethodNormalForm:
    def __init__(self, normal_form: str, sknf_or_sdnf: str):
        self.__normal_form_type: str = sknf_or_sdnf
        self.__normal_form: str = normal_form
        self.__subexpressions: list[str] = self.form_subexpressions()
        self.__subexpressions_arguments: list[list[str]] = self.form_subexpressions_arguments()
        self.__subexpressions_values: list[list[int]] = self.form_subexpressions_values()
        self.__father_indexes: dict = {self.__subexpressions_arguments[i].__str__(): [i]
                                       for i in range(len(self.__subexpressions_arguments))}

        self.__subexpressions_arguments_after_gluing, \
            self.__subexpressions_values_after_gluing = self.form_gluing()

    def form_subexpressions(self) -> list[str]:
        subexpressions: list[str] = []
        subexpression: str = ''
        sign = '|' if self.__normal_form_type == 'sdnf' else '&'
        for i in range(len(self.__normal_form)):
            if self.__normal_form[i] == sign:
                subexpressions.append(subexpression)
                subexpression = ''
                continue
            subexpression += self.__normal_form[i]
        if subexpression != '':
            subexpressions.append(subexpression)
        return subexpressions

    def form_subexpressions_arguments(self) -> list[list[str]]:
        subexpressions_arguments: list[list[str]] = [[] for i in range(len(self.__subexpressions))]
        for i in range(len(self.__subexpressions)):
            subexpression = self.__subexpressions[i]
            for j in range(len(subexpression)):
                if 'a' <= subexpression[j] <= 'z':
                    subexpressions_arguments[i].append(subexpression[j] if subexpression[j - 1] != '-'
                                                       else ('(' + subexpression[j - 1] + subexpression[j] + ')'))
        return subexpressions_arguments

    def form_subexpressions_values(self) -> list[list[int]]:
        subexpressions_values: list[list[int]] = [[] for i in range(len(self.__subexpressions))]
        for i in range(len(self.__subexpressions_arguments)):
            for argument in self.__subexpressions_arguments[i]:
                if len(argument) == 1:
                    subexpressions_values[i].append(1)
                else:
                    subexpressions_values[i].append(0)
        return subexpressions_values

    def form_gluing(self) -> (list[list[str]], list[list[bool]]):
        arguments, values = self.__subexpressions_arguments, self.__subexpressions_values
        quit_from_loop = False
        while not quit_from_loop:
            arguments, values, quit_from_loop = self.gluing(arguments, values)
        old_values, old_arguments = values.copy(), arguments.copy()
        for i in range(len(old_values)):
            count_minus_1: int = 0
            for j in old_values[i]:
                if j == -1:
                    count_minus_1 += 1
            if len(old_values[i]) - count_minus_1 != len(old_arguments[i]):
                values.remove(old_values[i])
                arguments.remove(old_arguments[i])
        return arguments, values

    def gluing(self, expressions_arguments: list[list[str]], expressions_values: list[list[int]]) \
            -> (list[list[str]], bool):
        gluing_arguments: list[list[str]] = []
        gluing_values: list[list[int]] = []
        quit_from_loop = False
        used: list[bool] = [False for i in range(len(expressions_values))]
        for i in range(len(expressions_values)):
            for j in range(i + 1, len(expressions_values)):
                check: (bool, int, int) = self.ready_for_gluing(expressions_values[i], expressions_values[j],
                                                                len(expressions_arguments[i]) - 1)
                if check[0]:
                    gluing_father_indexes: list[int] = self.__father_indexes[expressions_arguments[i].__str__()][:]
                    j_father_indexes: list[int] = self.__father_indexes[expressions_arguments[j].__str__()]
                    for index in j_father_indexes:
                        if index not in gluing_father_indexes:
                            gluing_father_indexes.append(index)

                    used[i], used[j] = True, True
                    temp_gluing_arguments, temp_gluing_values = self.get_gluing_lists(expressions_arguments[i],
                                                                                      expressions_values[i], check[1],
                                                                                      check[2])
                    gluing_arguments.append(temp_gluing_arguments)
                    gluing_values.append(temp_gluing_values)
                    self.__father_indexes[temp_gluing_arguments.__str__()] = gluing_father_indexes
        not_used_amount: int = 0
        for i in range(len(used)):
            if not used[i]:
                not_used_amount += 1
                gluing_arguments.append(expressions_arguments[i])
                gluing_values.append(expressions_values[i])
        if not_used_amount == len(used):
            quit_from_loop = True
        return gluing_arguments, gluing_values, quit_from_loop

    @staticmethod
    def ready_for_gluing(first_expression_values: list[int], second_expression_values: list[int], goal: int) \
            -> (bool, int, int):
        if minus_indexes(first_expression_values) != minus_indexes(second_expression_values):
            return False, 0
        difference_value_position: int = 0
        equal_amount: int = 0
        for i in range(len(first_expression_values)):
            if ((first_expression_values[i] != -1 and second_expression_values[i] != -1) and
                    (first_expression_values[i] == second_expression_values[i])):
                equal_amount += 1
            elif ((first_expression_values[i] != -1 and second_expression_values[i] != -1) and
                  (first_expression_values[i] != second_expression_values[i])):
                difference_value_position = i
        minuses_amount_before_difference: int = 0
        for i in range(difference_value_position):
            if first_expression_values[i] == -1:
                minuses_amount_before_difference += 1
        if equal_amount != goal:
            return False, 0
        return True, difference_value_position, difference_value_position - minuses_amount_before_difference

    @staticmethod
    def get_gluing_lists(expression_arguments: list[str], expression_values: list[int], difference_value_position: int,
                         difference_arguments_position) -> (list[str], list[bool]):
        gluing_arguments: list[str] = []
        gluing_values: list[int] = expression_values[:]
        for i in range(len(expression_arguments)):
            if i != difference_arguments_position:
                gluing_arguments.append(expression_arguments[i])
            elif i == difference_value_position:
                gluing_values[i] = -1
        return gluing_arguments, gluing_values

    def normal_form_without_one_implicate(self, position: int) -> str:
        normal_form: str = ''
        new_subexpressions: list[list[str]] = []
        sign: str = '|' if self.__normal_form_type == 'sdnf' else '&'
        nested_sign: str = '&' if self.__normal_form_type == 'sdnf' else '|'
        for i in range(len(self.__subexpressions_arguments_after_gluing)):
            if i == position:
                continue
            new_subexpressions.append(self.__subexpressions_arguments_after_gluing[i])
        for i in range(len(new_subexpressions) - 1):
            nested_sndf = ''
            for j in range(len(new_subexpressions[i]) - 1):
                nested_sndf += '(' + new_subexpressions[i][j] + nested_sign
            nested_sndf += new_subexpressions[i][len(new_subexpressions[i]) - 1]
            for j in range(len(new_subexpressions[i]) - 1):
                nested_sndf += ')'
            normal_form += '(' + nested_sndf + sign
        nested_sndf = ''
        for j in range(len(new_subexpressions[len(new_subexpressions) - 1]) - 1):
            nested_sndf += '(' + new_subexpressions[len(new_subexpressions) - 1][j] + nested_sign
        nested_sndf += new_subexpressions[len(new_subexpressions) - 1][len(new_subexpressions
                                                                           [len(new_subexpressions) - 1]) - 1]
        for j in range(len(new_subexpressions[len(new_subexpressions) - 1]) - 1):
            nested_sndf += ')'
        empty_normal_form = len(normal_form) == 0
        normal_form += ('(' if empty_normal_form else '') + nested_sndf
        for i in range(len(new_subexpressions) - 1 + int(empty_normal_form)):
            normal_form += ')'
        if len(new_subexpressions) == 1:
            normal_form = normal_form[1:len(normal_form) - 1]
        return normal_form

    def final_normal_form(self):
        if len(self.__subexpressions_arguments_after_gluing) == 1:
            return
        copy: list[list[str]] = self.__subexpressions_arguments_after_gluing[:]
        values: list[bool] = LogicalExpression(self.normal_form_without_one_implicate(-1)).final_values()
        for i in copy:
            if (LogicalExpression(self.normal_form_without_one_implicate(
                    self.__subexpressions_arguments_after_gluing.index(i))).final_values() == values and
                    i in self.__subexpressions_arguments_after_gluing):
                self.__subexpressions_arguments_after_gluing.remove(i)

    @property
    def subexpressions(self) -> list[str]:
        return self.__subexpressions

    @property
    def subexpressions_arguments(self) -> list[list[str]]:
        return self.__subexpressions_arguments

    @property
    def subexpressions_values(self) -> list[list[int]]:
        return self.__subexpressions_values

    @property
    def subexpressions_arguments_after_gluing(self) -> list[list[str]]:
        return self.__subexpressions_arguments_after_gluing

    @property
    def father_indexes(self) -> dict:
        return self.__father_indexes

    @property
    def normal_form_type(self) -> str:
        return self.__normal_form_type


def minus_indexes(values) -> list[int]:
    minuses: list[int] = []
    for i in range(len(values)):
        if values[i] == -1:
            minuses.append(i)
    return minuses
