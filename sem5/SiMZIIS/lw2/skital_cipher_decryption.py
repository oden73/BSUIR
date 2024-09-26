import math


class SkitalCipherDecryption:
    def __init__(self, encrypted_message: str, rows: int, columns: int) -> None:
        self.__rows: int = rows
        self.__columns: int = columns

        self.__matrix_list: list[list[list[str]]] = [[['' for _ in range(self.__columns)] for _ in range(self.__rows)]
                                                     for _ in range(math.ceil(len(encrypted_message) /
                                                                              (rows * columns)))]

        difference: int = (self.__rows * self.__columns) - len(encrypted_message) % (self.__rows * self.__columns)
        if difference == self.__rows * self.__columns:
            difference = 0

        for i in range(self.__rows - 1, -1, -1):
            for j in range(self.__columns - 1, -1, -1):
                if difference == 0:
                    break

                self.__matrix_list[len(self.__matrix_list) - 1][i][j] = '#'
                difference -= 1

        str_index = 0
        for k in range(self.__columns):
            for i in range(len(self.__matrix_list)):
                end: bool = False
                for j in range(self.__rows):
                    if self.__matrix_list[i][j][k] == '#':
                        end = True
                        break

                    self.__matrix_list[i][j][k] = encrypted_message[str_index]
                    str_index += 1

                if end:
                    break

    def decrypted_message(self) -> str:
        decrypted_message: str = ''

        for i in range(len(self.__matrix_list)):
            for j in range(self.__rows):
                for k in range(self.__columns):
                    if self.__matrix_list[i][j][k] != '#':
                        decrypted_message += self.__matrix_list[i][j][k]

        return decrypted_message
