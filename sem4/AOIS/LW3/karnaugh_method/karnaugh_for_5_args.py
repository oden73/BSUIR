from logical_expression.LogicalExpression import LogicalExpression


class KarnaughFor5Arguments:
    def __init__(self, logical_expression: LogicalExpression, sdnf_or_sknf: str):
        self.__logical_expression: LogicalExpression = logical_expression
        self.__arguments: list[str] = list(logical_expression.form_indexes_and_values_dict()[0].keys())
        self.__truth_table_values: list[int] = logical_expression.final_values()
        self.__top_row: list[list[str]] = [
            ['0', '0', '0', '0', '1', '1', '1', '1'],
            ['0', '0', '1', '1', '1', '1', '0', '0'],
            ['0', '1', '1', '0', '0', '1', '1', '0']
        ]
        self.__left_column: list[list[str]] = [
            ['0', '0', '1', '1'],
            ['0', '1', '1', '0']
        ]
        self.__index_order: list[int] = []
        self.__table: list[list[int]] = self.form_table()
        self.__table_left_half: list[list[int]] = []
        self.__table_right_half: list[list[int]] = []
        self.__table_left_half, self.__table_right_half = self.form_halfs()
        self.__sdnf_of_sdnf: str = sdnf_or_sknf

    def form_table(self) -> list[list[int]]:
        for i in range(len(self.__left_column[0])):
            for j in range(len(self.__top_row[0])):
                self.__index_order.append(self.decimal_view(self.__left_column[0][i] + self.__left_column[1][i]
                                                            + self.__top_row[0][j] + self.__top_row[1][j] +
                                                            self.__top_row[2][j]))
        table: list[list[int]] = []
        index: int = 0
        for i in range(len(self.__left_column[0])):
            table.append([])
            for j in range(len(self.__top_row[0])):
                table[i].append(self.__truth_table_values[self.__index_order[index]])
                index += 1
        return table

    def form_halfs(self) -> (list[list[int]], list[list[int]]):
        right_half: list[list[int]] = []
        left_half: list[list[int]] = []
        for i in self.__table:
            left_half.append([i[j] for j in range(4)])
            right_half.append([i[j] for j in range(4, len(i))])
        return left_half, right_half

    def form_final_normal_form_fields(self) -> list[list[tuple]]:
        used_indexes: list[tuple] = []
        fields: list[list[tuple]] = []
        value: int = 1 if self.__sdnf_of_sdnf == 'sdnf' else 0
        for i in range(len(self.__table)):
            for j in range(len(self.__table[0])):
                if len(fields) == 2:
                    print(123)
                if not (i, j) in used_indexes and self.__table[i][j] == value:
                    half = self.__table_left_half if j < 4 else self.__table_right_half
                    side: str = 'left' if j < 4 else 'right'
                    field = self.form_field(half, (i, j % 4), value, side)
                    fields.append(field)
                    for index in field:
                        if index not in used_indexes:
                            used_indexes.append(index)
        return fields

    def form_field(self, half: list[list[int]], initial_index: tuple, value: int, side: str) -> list[tuple]:
        one_half_field: list[tuple] = self.form_field_in_half(half, initial_index, value)
        fixed_one_half_field: list[tuple] = []
        if side == 'right':
            for i in one_half_field:
                fixed_one_half_field.append((i[0], i[1] + len(half)))
        else:
            fixed_one_half_field = one_half_field
        other_half: list[list[int]] = self.__table_right_half if side == 'left' else self.__table_left_half
        total_field: list[tuple] = self.find_equivalence_in_other_half(other_half, fixed_one_half_field, value)
        return total_field

    def form_field_in_half(self, half: list[list[int]], initial_index: tuple, value: int) -> list[tuple]:
        possible_way_to_spread: dict = {
            'right': True,
            'left': True,
            'top': True,
            'down': True
        }
        degrees = [1, 2, 4, 8, 16, 32]
        field: list[tuple] = [initial_index]
        while possible_way_to_spread['top']:
            last: tuple = field[len(field) - 1]
            if possible_way_to_spread['right']:
                if last[1] <= len(half[0]) - 2:
                    if half[last[0]][last[1] + 1] == value and (last[0], last[1] + 1) not in field:
                        field.append((last[0], last[1] + 1))
                    else:
                        if len(field) not in degrees:
                            field = self.fix_index_list(field, False)
                        possible_way_to_spread['right'] = False
                else:
                    if half[last[0]][0] == value and (last[0], 0) not in field:
                        field.append((last[0], 0))
                    else:
                        if len(field) not in degrees:
                            field = self.fix_index_list(field, False)
                        possible_way_to_spread['right'] = False
            elif possible_way_to_spread['left']:
                last = field[0]
                if last[1] >= 1:
                    if half[last[0]][last[1] - 1] == value and (last[0], last[1] - 1) not in field:
                        field.insert(0, (last[0], last[1] - 1))
                    else:
                        if len(field) not in degrees:
                            field = self.fix_index_list(field, True)
                        possible_way_to_spread['left'] = False
                else:
                    if (half[last[0]][len(half[0]) - 1] == value and (last[0], len(half[0]) - 1)
                            not in field):
                        field.insert(0, (last[0], len(half[0]) - 1))
                    else:
                        if len(field) not in degrees:
                            field = self.fix_index_list(field, True)
                        possible_way_to_spread['left'] = False
            elif possible_way_to_spread['down']:
                new_indexes = self.possibility_to_go_down(half, field, value)
                field += new_indexes
                if len(field) not in degrees:
                    field = self.fix_index_list(field, False)
                possible_way_to_spread['down'] = False
            elif possible_way_to_spread['top']:
                new_indexes = self.possibility_to_go_top(half, field, value)
                field += new_indexes
                if len(field) not in degrees:
                    field = self.fix_index_list(field, False)
                possible_way_to_spread['top'] = False
        return field

    def form_final_normal_form_arguments(self) -> list[list[str]]:
        fields: list[list[tuple]] = self.form_final_normal_form_fields()
        value: str = '1' if self.__sdnf_of_sdnf == 'sdnf' else '0'
        arguments: list[list[str]] = []
        for i in range(len(fields)):
            initial_values: list[str] = [self.__left_column[0][fields[i][0][0]], self.__left_column[1][fields[i][0][0]],
                                         self.__top_row[0][fields[i][0][1]], self.__top_row[1][fields[i][0][1]],
                                         self.__top_row[2][fields[i][0][1]]]
            changes: list[bool] = [False, False, False, False, False]
            for j in fields[i]:
                if self.__top_row[2][j[1]] != initial_values[4]:
                    changes[4] = True
                if self.__top_row[1][j[1]] != initial_values[3]:
                    changes[3] = True
                elif self.__top_row[0][j[1]] != initial_values[2]:
                    changes[2] = True
                elif self.__left_column[1][j[0]] != initial_values[1]:
                    changes[1] = True
                elif self.__left_column[0][j[0]] != initial_values[0]:
                    changes[0] = True
            field_arguments: list[str] = []
            for j in range(len(changes)):
                if not changes[j]:
                    field_arguments.append(self.__arguments[j] if initial_values[j] == value
                                           else '(-' + self.__arguments[j] + ')')
            arguments.append(field_arguments)
        return arguments

    @staticmethod
    def possibility_to_go_top(half: list[list[int]], indexes: list[tuple], value: int) -> list[tuple]:
        last_row_indexes: list[tuple] = []
        last_row_index: int = indexes[0][0]
        for i in range(len(indexes)):
            if last_row_index != indexes[i][0]:
                break
            last_row_indexes.append(indexes[i])
        row_to_check: int = len(half) - 1 if last_row_indexes[0][0] == 0 else last_row_indexes[0][0] - 1
        continue_going: bool = True
        new_indexes: list[tuple] = []
        while continue_going:
            for i in range(len(last_row_indexes)):
                if (half[row_to_check][last_row_indexes[i][1]] == 1 - value or
                        (row_to_check, last_row_indexes[i][1]) in new_indexes or
                        (row_to_check, last_row_indexes[i][1]) in indexes):
                    continue_going = False
                    break
            if continue_going:
                for i in range(len(last_row_indexes)):
                    new_indexes.append((row_to_check, last_row_indexes[i][1]))
                row_to_check = len(half) - 1 if row_to_check == 0 else row_to_check - 1
        return new_indexes

    @staticmethod
    def possibility_to_go_down(half: list[list[int]], indexes: list[tuple], value: int) -> (bool, list[tuple]):
        last_row_indexes: list[tuple] = []
        last_row_index: int = indexes[len(indexes) - 1][0]
        for i in range(len(indexes) - 1, -1, -1):
            if last_row_index != indexes[i][0]:
                break
            last_row_indexes.append(indexes[i])
        row_to_check: int = 0 if last_row_indexes[0][0] == len(half) - 1 else last_row_indexes[0][0] + 1
        continue_going: bool = True
        new_indexes: list[tuple] = []
        while continue_going:
            for i in range(len(last_row_indexes)):
                if (half[row_to_check][last_row_indexes[i][1]] == 1 - value or
                        (row_to_check, last_row_indexes[i][1]) in new_indexes or
                        (row_to_check, last_row_indexes[i][1]) in indexes):
                    continue_going = False
                    break
            if continue_going:
                for i in range(len(last_row_indexes)):
                    new_indexes.append((row_to_check, last_row_indexes[i][1]))
                row_to_check = 0 if row_to_check == len(half) - 1 else row_to_check + 1
        return new_indexes

    # @staticmethod
    def find_equivalence_in_other_half(self, half: list[list[int]], indexes: list[tuple], value: int) -> list[tuple]:
        other_half_indexes: list[tuple] = []
        for index in indexes:
            y: int = (len(self.__table) - 1 - index[1]) % len(half[0])
            if half[index[0]][len(half[0]) - 1 - (index[1] % len(half[0]))] == value:
                # other_half_indexes.append((index[0], len(half[0]) - 1 - (index[1] % len(half[0]))))
                other_half_indexes.append((index[0], len(self.__table[0]) - 1 - index[1]))
            else:
                return indexes
        indexes += other_half_indexes
        return indexes

    def final_normal_form(self) -> str:
        arguments = self.form_final_normal_form_arguments()
        if len(arguments) == 1 and len(arguments[0]) == 0:
            return 'normal form is empty'
        normal_form = ''
        nested_sign: str = '&' if self.__sdnf_of_sdnf == 'sdnf' else '|'
        sign: str = '|' if self.__sdnf_of_sdnf == 'sdnf' else '&'
        for i in range(len(arguments)):
            if len(arguments[i]) == 1 and len(arguments[i][0]) == 4:
                normal_form += arguments[i][0]
                if i != len(arguments) - 1:
                    normal_form += sign
                continue
            normal_form += '(' + arguments[i][0]
            for j in range(1, len(arguments[i])):
                normal_form += nested_sign + arguments[i][j]
            normal_form += ')'
            if i != len(arguments) - 1:
                normal_form += sign
        if len(arguments) > 1:
            normal_form = '(' + normal_form + ')'
        return normal_form

    def print_table(self):
        row_print = '     ' + self.__arguments[2]
        for i in self.__top_row[0]:
            row_print += '   ' + i
        print(row_print)

        row_print = '     ' + self.__arguments[3]
        for i in self.__top_row[1]:
            row_print += '   ' + i
        print(row_print)

        row_print = ' ' + self.__arguments[0] + ' ' + self.__arguments[1] + '\\' + self.__arguments[4]
        for i in self.__top_row[2]:
            row_print += '   ' + i
        print(row_print)

        number_of_minuses: int = len(row_print)
        row_print = ''
        for i in range(number_of_minuses):
            row_print += '-'
        print(row_print)

        for i in range(len(self.__left_column[0])):
            row_print = '  ' + self.__left_column[0][i] + ' ' + self.__left_column[1][i] + ' '
            for j in range(len(self.__top_row[0])):
                row_print += ' | ' + str(self.__table[i][j])
            print(row_print)

    @staticmethod
    def fix_index_list(index_list: list[tuple], start_or_end: bool):
        degrees = [1, 2, 4, 8, 16, 32]
        while len(index_list) not in degrees:
            if start_or_end:
                index_list.pop(0)
            else:
                index_list.pop(len(index_list) - 1)
        return index_list
    @staticmethod
    def decimal_view(value: str) -> int:
        if value.count('0') == len(value):
            return 0
        while value[0] == '0':
            value = value[1:]
        decimal_value: int = 0
        for i in range(len(value) - 1, -1, -1):
            decimal_value += int(value[i]) * pow(2, len(value) - 1 - i)
        return decimal_value
