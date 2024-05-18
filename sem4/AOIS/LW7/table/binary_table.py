from table.logical_functions import LogicalFunctions


class BinaryTable:
    def __init__(self):
        self.logical_functions: LogicalFunctions = LogicalFunctions()
        self.table: list[list[int]] = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def get_word_by_index(self, index: int) -> list[int]:
        word: list[int] = []

        for i in range(index, len(self.table)):
            word.append(self.table[i][index])

        for i in range(index):
            word.append(self.table[i][index])

        return word

    def update_word_by_index(self, new_word: str, index: int) -> None:
        for i in range(index, len(self.table)):
            self.table[i][index] = int(new_word[i - index])

        for i in range(index):
            self.table[i][index] = int(new_word[len(self.table) - index + i])

    def get_address_column_by_index(self, index: int) -> list[int]:
        word: list[int] = []

        for i in range(index, len(self.table)):
            word.append(self.table[i][i - index])

        for i in range(index):
            word.append(self.table[i][len(self.table) - index + i])

        return word

    def update_address_column_by_index(self, new_address_column: str, index: int) -> None:
        for i in range(index, len(self.table)):
            self.table[i][i - index] = int(new_address_column[i - index])

        for i in range(index):
            self.table[i][len(self.table) - index + i] = int(new_address_column[len(self.table) - index + i])

    def logical_operation(self, index1: int, index2: int, index_where_to_write: int, operation_string: str) -> None:
        word1, word2 = self.get_word_by_index(index1), self.get_word_by_index(index2)

        word_to_update: list[int] = []
        for i in range(len(self.table)):
            word_to_update.append(self.logical_functions.return_value(operation_string, word1[i], word2[i]))

        word_to_update_str: str = self.get_word_str(word_to_update)
        self.update_word_by_index(word_to_update_str, index_where_to_write)

    def sort(self) -> None:
        sort_helper_list: list[tuple] = []
        for i in range(len(self.table)):
            word: list[int] = self.get_word_by_index(i)
            word_str: str = self.get_word_str(word)
            value: int = self.decimal_view(word_str)
            sort_helper_list.append((value, word_str))

        sort_helper_list.sort(key=lambda a: a[0])

        for i in range(len(sort_helper_list)):
            self.update_word_by_index(sort_helper_list[i][1], i)

    def word_sum(self, key_string: str) -> None:
        words_to_update: list[tuple] = []

        for i in range(len(self.table)):
            word: list[int] = self.get_word_by_index(i)
            word_str: str = self.get_word_str(word)

            if word_str[:len(key_string)] == key_string:
                words_to_update.append((word_str, i))

        for i in range(len(words_to_update)):
            word_to_update, index = words_to_update[i]

            a, b = (word_to_update[len(key_string):len(key_string) + 4],
                    word_to_update[len(key_string) + 4:len(key_string) + 8])
            s: str = self.binary_view(self.decimal_view(a) + self.decimal_view(b))

            new_word: str = key_string + a + b + s
            self.update_word_by_index(new_word, index)

    @staticmethod
    def get_word_str(word: list[int]) -> str:
        word_str: str = ''

        for number in word:
            word_str += str(number)

        return word_str

    @staticmethod
    def decimal_view(binary_number: str) -> int:
        value: int = 0

        for i in range(len(binary_number) - 1, -1, -1):
            value += int(binary_number[i]) * pow(2, len(binary_number) - 1 - i)

        return value

    @staticmethod
    def binary_view(number: int) -> str:
        binary_number: str = ''

        while number > 0:
            binary_number = str(number % 2) + binary_number
            number //= 2

        return binary_number if len(binary_number) == 5 else '0' + binary_number
