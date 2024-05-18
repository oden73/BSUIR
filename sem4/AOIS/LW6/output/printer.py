class Printer:
    def __init__(self):
        pass

    @staticmethod
    def print_operation_header() -> None:
        print('Выберите операцию:')
        print('1 - вывод хеш-таблицы')
        print('2 - добавление элемента в хеш-таблицу')
        print('3 - поиск элемента в хеш таблице по ключу')
        print('4 - обновление данных элемента в хеш-таблице по ключу')
        print('5 - удаление элемента из хеш-таблицы по ключу')
        print('0 - выход')

    @staticmethod
    def print_hash_table(hash_table: list[tuple]) -> None:
        spaces = [1, 1, 1, 1, 1, 1]
        for element in hash_table:
            for i in range(len(element)):
                spaces[i] = max(spaces[i], len(element[i]))

        print_string = ''

        header: list[str] = ['ID', 'V', 'h', 'U', 'HTID', 'Pi']
        for i in range(len(header)):
            print_string += header[i]
            for j in range(max(0, spaces[i] - len(header[i])) + 1):
                print_string += ' '

        print(print_string)
        print_string = ''

        for element in hash_table:
            for i in range(len(element)):
                print_string += element[i]
                for j in range(abs(spaces[i] - len(element[i])) + 1):
                    print_string += ' '

            print(print_string)
            print_string = ''

    @staticmethod
    def print_operation_complete() -> None:
        print('Операция завершена успешно')

    @staticmethod
    def print_element_not_found() -> None:
        print('Элемент с таким ID не был найден, так что операцию завершить не удалось')

    @staticmethod
    def print_add_element() -> None:
        print('Введите ID и Pi элемента, который вы хотите добавить:')

    @staticmethod
    def print_search_element() -> None:
        print('Введите ID элемента, который вы хотите найти:')

    @staticmethod
    def print_search_result(Pi: str) -> None:
        print(f'Pi искомого элемента: {Pi}')

    @staticmethod
    def print_update_element() -> None:
        print('Введите ID элемента, значение которого вы хотите обновить, и Pi, которое хотите установить:')

    @staticmethod
    def print_delete_element() -> None:
        print('Введите ID элемента, который вы хотите удалить:')

    @staticmethod
    def print_unknown_operation() -> None:
        print('Неизвестная операция, попробуйте еще раз')
