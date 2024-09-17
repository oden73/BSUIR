from password import Password


password_len: int = int(input('Введите количество символов в пароле: '))

password: Password = Password(password_len)
print('Сгенерированный пароль:', password.password)
