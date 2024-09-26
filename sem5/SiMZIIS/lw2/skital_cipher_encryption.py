import math


class SkitalCipherEncryption:
    def __init__(self, message: str, rows: int, columns: int) -> None:
        message = message.replace(' ', '')

        self.__matrix_list: list[list[list[str]]] = [[] for _ in range(math.ceil(len(message) / (rows * columns)))]
        self.__rows: int = rows
        self.__columns: int = columns

        message_blocks: list[str] = []
        for i in range(0, len(message), self.__rows * self.__columns):
            message_blocks.append(message[i:i + self.__rows * self.__columns])

        for i in range(len(message_blocks)):
            self.__matrix_list[i] = self.encryption(message_blocks[i])



    def encryption(self, message_part: str) -> list[list[str]]:
        matrix: list[list[str]] = [['' for _ in range(self.__columns)] for _ in range(self.__rows)]

        for i in range(len(message_part)):
            matrix[i // self.__columns][i % self.__columns] = message_part[i]

        if len(message_part) < self.__rows * self.__columns:
            for i in range(len(message_part), self.__rows * self.__columns):
                matrix[i // self.__columns][i % self.__columns] = '#'

        return matrix

    def encrypted_message(self) -> str:
        encrypted_message: str = ''

        for k in range(self.__columns):
            for i in range(len(self.__matrix_list)):
                for j in range(self.__rows):
                    if self.__matrix_list[i][j][k] != '#':
                        encrypted_message += self.__matrix_list[i][j][k]

        return encrypted_message


        # for i in range(len(self.__matrix_list)):
        #     for j in range(len(self.__matrix_list[i])):
        #         output: str = ''
        #         for k in range(len(self.__matrix_list[i][j])):
        #             output += self.__matrix_list[i][j][k]
        #         print(output)
        #     print('----------')