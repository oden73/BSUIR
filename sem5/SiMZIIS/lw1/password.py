import random


class Password:
    symbols_list: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                               'T', 'V', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
                               '5', '6', '7', '8', '9']

    def __init__(self, symbols_amount: int) -> None:
        self.__password: str = ''
        for _ in range(symbols_amount):
            self.__password += random.choice(Password.symbols_list)

    @property
    def password(self) -> str:
        return self.__password
