import time

from skital_cipher_encryption import SkitalCipherEncryption
from skital_cipher_decryption import SkitalCipherDecryption
from skital_cipher_hack import SkitalCipherHack

start_time = time.process_time()

message: str = input('Введите сообщение: ')
rows: int = int(input('Введите количество строк в таблице: '))
columns: int = int(input('Введите количество столбцов в таблице: '))

enc: SkitalCipherEncryption = SkitalCipherEncryption(message, rows, columns)
enc_str: str = enc.encrypted_message()

dec: SkitalCipherDecryption = SkitalCipherDecryption(enc_str, rows, columns)
dec_str: str = dec.decrypted_message()

print(f'Зашифрованная строка: {enc_str}')
# print(f'Расшифрованная строка: {dec_str}')

hack: SkitalCipherHack = SkitalCipherHack(enc_str)
options: list[str] = hack.search()

for i in options:
    if i == message:
        end_time = time.process_time()
        exec_time = (end_time - start_time) * 1000

        print(f'Искомое сообщение: {i}, было найдено за {exec_time:.2f} милисекунд')
        exit(0)