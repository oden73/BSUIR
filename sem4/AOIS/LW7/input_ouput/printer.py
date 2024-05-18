class Printer:
    def __init__(self):
        pass

    @staticmethod
    def print_operations() -> None:
        print('Введите номер операции, которую хотите совершить:')
        print('1 - вывод таблицы')
        print('2 - вывод слова по индексу')
        print('3 - изменение слова по индексу')
        print('4 - вывод адресного столбца по индексу')
        print('5 - изменение адресного столбца по индексу')
        print('6 - выполнение логических функций над двумя словами и запись в третье')
        print('7 - сортировка таблицы')
        print('8 - арифметические операции над полями слов')
        print('0 - выход')

    @staticmethod
    def unknown_operation() -> None:
        print('Неизвестный номер операции, попробуйте еще раз')

    @staticmethod
    def operation_complete() -> None:
        print('Операция завершена успешно')

    @staticmethod
    def print_table(table: list[list[int]]) -> None:
        for i in range(len(table)):
            print_string: str = ''
            for j in range(len(table[i])):
                print_string += str(table[i][j]) + '  '
            print(print_string)

    @staticmethod
    def print_get_word_by_index() -> None:
        print('Введите индекс слова, которое хотите получить:')

    @staticmethod
    def print_word_by_index(word: str) -> None:
        print(f'Искомое слово: {word}')

    @staticmethod
    def print_update_word_by_index() -> None:
        print('Введите индекс слова, которое хотите изменить,  и новое слово:')

    @staticmethod
    def print_get_address_column_by_index() -> None:
        print('Введите индекс адресного столбца, который хотите получить:')

    @staticmethod
    def print_address_column_by_index(address_column: str) -> None:
        print(f'Искомый адресный столбец: {address_column}')

    @staticmethod
    def print_update_address_column_by_index() -> None:
        print('Введите индекс адресного столбца, который хотите изменить, и новый адресный столбец:')

    @staticmethod
    def print_logical_functions() -> None:
        print('Введите индексы двух слов, над которыми будут совершены операции, индекс слова, в который будет '
              'записан результат, и логическую функцию:')

    @staticmethod
    def print_string_key() -> None:
        print('Введите ключ V, согласно которому будут изменены поля слов, у которых первые 3 бита совпадают с ключом:')
