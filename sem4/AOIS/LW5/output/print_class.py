from karnaugh.karnaugh_for_4_args import KarnaughFor4Arguments

digital_device_table_truth: list[list[int]] = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],  # q3'
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],  # q2'
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],  # q1'
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],  # V
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # q3
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0],  # q2
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],  # q1
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],  # h3
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # h2
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]   # h1
]


class Print:
    def __init__(self):
        self.__digital_device_truth_table: list[list[int]] = digital_device_table_truth

    def print_digital_device_truth_table(self) -> None:
        print('Таблица истинности цифрового устройства')
        arguments: list[str] = ['q3\'', 'q2\'', 'q1\'', 'V  ', 'q3 ', 'q2 ', 'q1 ', 'h3 ', 'h2 ', 'h1 ']
        for i in range(len(self.__digital_device_truth_table)):
            print_string: str = arguments[i] + ' |'
            for j in range(len(self.__digital_device_truth_table[i])):
                print_string += f' {self.__digital_device_truth_table[i][j]}'
            print(print_string)

    def print_h3_minimization(self) -> None:
        print('Минимизация h3:')
        truth_table_str: str = ''
        for i in range(len(self.__digital_device_truth_table[7])):
            truth_table_str += self.__digital_device_truth_table[7][i].__str__()
        karnaugh: KarnaughFor4Arguments = KarnaughFor4Arguments(truth_table_str, 'sdnf')
        print(karnaugh.final_normal_form())

    def print_h2_minimization(self) -> None:
        print('Минимизация h2:')
        truth_table_str: str = ''
        for i in range(len(self.__digital_device_truth_table[8])):
            truth_table_str += self.__digital_device_truth_table[8][i].__str__()
        karnaugh: KarnaughFor4Arguments = KarnaughFor4Arguments(truth_table_str, 'sdnf')
        print(karnaugh.final_normal_form())

    def print_h1_minimization(self) -> None:
        print('Минимизация h1:')
        truth_table_str: str = ''
        for i in range(len(self.__digital_device_truth_table[9])):
            truth_table_str += self.__digital_device_truth_table[9][i].__str__()
        karnaugh: KarnaughFor4Arguments = KarnaughFor4Arguments(truth_table_str, 'sdnf')
        print(karnaugh.final_normal_form())
