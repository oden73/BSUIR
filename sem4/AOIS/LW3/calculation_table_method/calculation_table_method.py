import math

from calculation_method.calculation_method import CalculationMethodNormalForm
from logical_expression.LogicalExpression import LogicalExpression


class CalculationTableMethodNormalForm:
    def __init__(self, calculation_form: CalculationMethodNormalForm):
        self.__calculation_form: CalculationMethodNormalForm = calculation_form
        self.__glued_arguments: list[list[str]] = calculation_form.subexpressions_arguments_after_gluing
        self.__father_indexes: dict = {}
        self.__final_arguments: list[list[str]] = []
        self.__normal_form_type = self.__calculation_form.normal_form_type

    def final_normal_form(self):
        primary_subexpressions: list[str] = self.__calculation_form.subexpressions
        # print(self.__glued_arguments)
        final_arguments_str: list[str] = [str(i) for i in self.__glued_arguments]
        # print(self.__calculation_form.father_indexes)
        self.__father_indexes = self.__calculation_form.father_indexes.copy()
        for i in self.__calculation_form.father_indexes.keys():
            if i not in final_arguments_str:
                self.__father_indexes.pop(i)
        # print(self.__father_indexes)
        subexpressions_counts: list[int] = [0 for i in range(len(primary_subexpressions))]
        for i in range(len(subexpressions_counts)):
            for j in self.__father_indexes.values():
                subexpressions_counts[i] += j.count(i)
        # print(subexpressions_counts)
        appending_indexes: list[int] = []
        for i in range(len(final_arguments_str)):
            if not self.check_if_not_necessary(subexpressions_counts, self.__father_indexes[final_arguments_str[i]]):
                appending_indexes.append(i)
        for i in appending_indexes:
            self.__final_arguments.append(self.__glued_arguments[i])
        # print(self.__final_arguments)

    @staticmethod
    def check_if_not_necessary(subexpression_count, father_indexes) -> bool:
        for i in father_indexes:
            if subexpression_count[i] < 2:
                return False
        return True

    def table_print(self):
        expressions_str: list[str] = [self.nested_expression_str(self.__glued_arguments[i])
                                      for i in range(len(self.__glued_arguments))]
        first_column_len: int = 0
        row_print: str = ''
        for i in expressions_str:
            first_column_len = max(first_column_len, len(i))
        for i in range(first_column_len):
            row_print += ' '
        expressions = self.__calculation_form.subexpressions
        for i in expressions:
            row_print += (' I ' + i)
        print(row_print)
        for i in range(len(expressions_str)):
            row_print = expressions_str[i]
            for spaces in range(first_column_len - len(expressions_str[i])):
                row_print += ' '
            for j in range(len(expressions)):
                row_print += ' I '
                half: int = math.ceil(len(expressions[j]) / 2) - 1
                for spaces in range(half):
                    row_print += ' '
                row_print += 'X' if j in self.__father_indexes[self.__glued_arguments[i].__str__()] else 'O'
                row_print += ' ' if len(expressions[j]) % 2 == 0 else ''
                for spaces in range(half):
                    row_print += ' '
            print(row_print)

    def nested_expression_str(self, expression_arguments: list[str]) -> str:
        if len(expression_arguments) == 1 and len(expression_arguments[0]) == 4:
            return expression_arguments[0]
        sign = '&' if self.__normal_form_type == 'sdnf' else '|'
        normal_form: str = '(' + expression_arguments[0]
        for i in range(1, len(expression_arguments)):
            normal_form += sign + expression_arguments[i]
        normal_form += ')'
        return normal_form

    def normal_form(self):
        return self.__calculation_form.normal_form_without_one_implicate(-1)

    @property
    def final_arguments(self) -> list[list[str]]:
        return self.__final_arguments

    @property
    def glued_arguments(self) -> list[list[str]]:
        return self.__glued_arguments

    @property
    def father_indexes(self) -> dict:
        return self.__father_indexes
