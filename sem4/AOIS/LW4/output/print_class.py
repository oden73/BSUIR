from karnaugh.karnaugh_for_3_args import KarnaughFor3Arguments
from karnaugh.karnaugh_for_4_args import KarnaughFor4Arguments

odv3_truth_table: list[list[int]] = [
    [0, 0, 0, 0, 1, 1, 1, 1],  # x1
    [0, 0, 1, 1, 0, 0, 1, 1],  # x2
    [0, 1, 0, 1, 0, 1, 0, 1],  # x3
    [0, 1, 1, 0, 1, 0, 0, 1],  # di
    [0, 1, 1, 1, 0, 0, 0, 1]   # bi+1
]

d8421_truth_table: list[list[int]] = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],  # A
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],  # B
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],  # C
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],  # D
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # A\'
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0],  # B\'
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],  # C\'
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]   # D\'
]


class Print:
    def __init__(self):
        self.__odv3_truth_table: list[list[int]] = odv3_truth_table
        self.__d8421_truth_table: list[list[int]] = d8421_truth_table

    def print_odv_truth_table(self) -> None:
        print('Таблица истинности для ОДВ-3:')
        print_string: str = '     I'
        for i in range(len(self.__odv3_truth_table[0])):
            print_string += f' {i}  '
        print(print_string)
        print_string = ''
        for i in range(38):
            print_string += '-'
        print(print_string)
        print_string = ''
        arguments: list[str] = ['x1  ', 'x2  ', 'x3  ', 'di  ', 'bi+1']
        for i in range(len(arguments)):
            print_string += f'{arguments[i]} I'
            for j in range(len(self.__odv3_truth_table[i])):
                print_string += f' {self.__odv3_truth_table[i][j]} I'
            print(print_string)
            print_string = ''

    def print_di_minimization(self) -> None:
        print('Минимизация для di:')
        table_truth_str: str = ''
        for i in range(len(self.__odv3_truth_table[3])):
            table_truth_str += self.__odv3_truth_table[3][i].__str__()
        karnaugh_sdnf: KarnaughFor3Arguments = KarnaughFor3Arguments(table_truth_str, 'sdnf')
        print('SDNF:')
        print(karnaugh_sdnf.final_normal_form())
        karnaugh_sknf: KarnaughFor3Arguments = KarnaughFor3Arguments(table_truth_str, 'sknf')
        print('SKNF:')
        print(karnaugh_sknf.final_normal_form())

    def print_bi1_minimization(self) -> None:
        print('Минимизация для bi+1:')
        table_truth_str: str = ''
        for i in range(len(self.__odv3_truth_table[4])):
            table_truth_str += self.__odv3_truth_table[4][i].__str__()
        karnaugh_sdnf: KarnaughFor3Arguments = KarnaughFor3Arguments(table_truth_str, 'sdnf')
        print('SDNF:')
        print(karnaugh_sdnf.final_normal_form())
        karnaugh_sknf: KarnaughFor3Arguments = KarnaughFor3Arguments(table_truth_str, 'sknf')
        print('SKNF:')
        print(karnaugh_sknf.final_normal_form())

    def print_d8421_truth_table(self) -> None:
        print('Таблица истинности для D8421+1')
        print_string: str = 'A \tB \tC \tD \tA\'\tB\'\tC\'\tD\'\t'
        print(print_string)
        print('------------------------------')
        print_string = ''
        for i in range(len(self.__d8421_truth_table[0])):
            for j in range(len(self.__d8421_truth_table)):
                print_string += f'{self.__d8421_truth_table[j][i]} \t'
            print(print_string)
            print_string = ''

    def print_a_increment_minimization(self) -> None:
        print('Минимизация для A\':')
        table_truth_str: str = ''
        for i in range(len(self.__d8421_truth_table[4])):
            table_truth_str += self.__d8421_truth_table[4][i].__str__()
        karnaugh: KarnaughFor4Arguments = KarnaughFor4Arguments(table_truth_str, 'sdnf')
        print('SDNF:')
        print(karnaugh.final_normal_form())
        karnaugh: KarnaughFor4Arguments = KarnaughFor4Arguments(table_truth_str, 'sknf')
        print('SKNF:')
        print(karnaugh.final_normal_form())

    def print_b_increment_minimization(self) -> None:
        print('Минимизация для B\':')
        table_truth_str: str = ''
        for i in range(len(self.__d8421_truth_table[5])):
            table_truth_str += self.__d8421_truth_table[5][i].__str__()
        karnaugh: KarnaughFor4Arguments = KarnaughFor4Arguments(table_truth_str, 'sdnf')
        print('SDNF:')
        print(karnaugh.final_normal_form())
        karnaugh: KarnaughFor4Arguments = KarnaughFor4Arguments(table_truth_str, 'sknf')
        print('SKNF:')
        print(karnaugh.final_normal_form())

    def print_c_increment_minimization(self) -> None:
        print('Минимизация для C\':')
        table_truth_str: str = ''
        for i in range(len(self.__d8421_truth_table[6])):
            table_truth_str += self.__d8421_truth_table[6][i].__str__()
        karnaugh: KarnaughFor4Arguments = KarnaughFor4Arguments(table_truth_str, 'sdnf')
        print('SDNF:')
        print(karnaugh.final_normal_form())
        karnaugh: KarnaughFor4Arguments = KarnaughFor4Arguments(table_truth_str, 'sknf')
        print('SKNF:')
        print(karnaugh.final_normal_form())

    def print_d_increment_minimization(self) -> None:
        print('Минимизация для D\':')
        table_truth_str: str = ''
        for i in range(len(self.__d8421_truth_table[7])):
            table_truth_str += self.__d8421_truth_table[7][i].__str__()
        karnaugh: KarnaughFor4Arguments = KarnaughFor4Arguments(table_truth_str, 'sdnf')
        print('SDNF:')
        print(karnaugh.final_normal_form())
        karnaugh: KarnaughFor4Arguments = KarnaughFor4Arguments(table_truth_str, 'sknf')
        print('SKNF:')
        print(karnaugh.final_normal_form())
