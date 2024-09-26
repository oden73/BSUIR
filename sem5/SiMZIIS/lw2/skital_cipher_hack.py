from skital_cipher_decryption import SkitalCipherDecryption


class SkitalCipherHack:
    def __init__(self, decrypted_message: str) -> None:
        self.__decrypted_message: str = decrypted_message

    def search(self) -> list[str]:
        options: list[str] = []

        for rows in range(1, len(self.__decrypted_message) + 1):
            for columns in range(1, len(self.__decrypted_message) + 1):
                decrypter: SkitalCipherDecryption = SkitalCipherDecryption(self.__decrypted_message, rows, columns)

                options.append(decrypter.decrypted_message())

        return options
