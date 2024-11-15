import random
import hashlib


class RSA:
    def __init__(self, bits=1024):
        self.bits = bits
        self.p = self.generate_prime(bits)
        self.q = self.generate_prime(bits)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = 65537
        self.d = self.multiplicative_inverse(self.e, self.phi)

    def is_prime(self, n, k=5):
        if n < 2:
            return False
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            if n < p * p:
                return True
            if n % p == 0:
                return False
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def generate_prime(self, bits):
        while True:
            n = random.getrandbits(bits) | (1 << bits - 1) | 1
            if self.is_prime(n):
                return n

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def multiplicative_inverse(self, e, phi):
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            else:
                gcd, x, y = extended_gcd(b % a, a)
                return gcd, y - (b // a) * x, x

        gcd, x, y = extended_gcd(e, phi)
        if gcd != 1:
            return None
        else:
            return x % phi

    def power_mod(self, base, exponent, mod):
        result = 1
        base = base % mod
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % mod
            exponent = exponent >> 1
            base = (base * base) % mod
        return result

    def save_keys(self, public_key_path, private_key_path):
        with open(public_key_path, "w", encoding='utf-8') as f:
            f.write(f"{self.e}\n{self.n}")
        with open(private_key_path, "w", encoding='utf-8') as f:
            f.write(f"{self.d}\n{self.n}")

    def encrypt(self, message, public_key_path):
        with open(public_key_path, "r", encoding='utf-8') as f:
            e, n = map(int, f.read().splitlines())
        encrypted_message = [self.power_mod(ord(char), e, n) for char in message]
        with open(f"text_files/encrypted_messages/encrypted_message{public_key_path[-5]}.txt", "w", encoding='utf-8') as f:
            f.write(" ".join(map(str, encrypted_message)))

    def decrypt(self, encrypted_message_path, private_key_path):
        with open(private_key_path, "r", encoding='utf-8') as f:
            d, n = map(int, f.read().splitlines())
        with open(encrypted_message_path, "r", encoding='utf-8') as f:
            encrypted_message = list(map(int, f.read().split()))
        decrypted_message = "".join(chr(self.power_mod(char, d, n)) for char in encrypted_message)
        with open(f"text_files/decrypted_messages/decrypted_message{private_key_path[-5]}.txt", "w", encoding='utf-8') as f:
            f.write(decrypted_message)

    def sign(self, message, private_key_path):
        with open(private_key_path, "r", encoding='utf-8') as f:
            d, n = map(int, f.read().splitlines())
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        signature = self.power_mod(h, d, n)
        with open(f"text_files/signatures/signature{private_key_path[-5]}.txt", "w", encoding='utf-8') as f:
            f.write(str(signature))

    def verify(self, message, signature_path, public_key_path):
        with open(public_key_path, "r", encoding='utf-8') as f:
            e, n = map(int, f.read().splitlines())
        with open(signature_path, "r", encoding='utf-8') as f:
            signature = int(f.read())
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        verified = self.power_mod(signature, e, n) == h
        if verified:
            print("Подпись действительна.")
        else:
            print("Подпись недействительна.")
