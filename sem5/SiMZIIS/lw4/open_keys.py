def pow_mod(a: int, b: int, P: int) -> int:
    result: int = 1
    a %= P

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % P

        b >>= 1
        a = (a ** 2) % P

    return result


def is_primitive_root(g: int, P: int) -> bool:
    powers: set = set()

    for i in range(1, P):
        power: int = pow_mod(g, i, P)
        powers.add(power)

    return len(powers) == P - 1


def find_primitive_root(P: int) -> int:
    for g in range(2, P):
        if is_primitive_root(g, P):
            return g

    return -1


def secret_generation(g: int, P: int) -> None:
    num1: int = 10
    num2: int = 20

    A: int = pow_mod(g, num1, P)
    B: int = pow_mod(g, num2, P)

    A_secret: int = pow_mod(B, num1, P)
    B_secret: int = pow_mod(A, num2, P)

    print(f'Приватный ключ Алисы (a): {num1}')
    print(f'Приватный ключ Боба (b): {num2}')

    print(f'Открытый ключ Алисы (g^a): {A}')
    print(f'Открытый ключ Алисы (g^b): {B}')

    print(f'Общий секрет (g^ab): {A_secret}')
    print(f'Общий секрет (g^ba): {B_secret}')


P = 8699
g: int = find_primitive_root(P)

if g == -1:
    print('Заданное число P не имеет примитивного корня')
    exit(0)

secret_generation(g, P)
