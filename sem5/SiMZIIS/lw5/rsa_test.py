import unittest
from rsa_encryption import RSA
import hashlib


class TestRSA(unittest.TestCase):
    def setUp(self):
        self.rsa = RSA()

    def test_encryption_decryption_and_signature1(self):
        message = "asd asd asd"
        self.rsa.save_keys("text_files/public_keys/public_key1.txt", "text_files/private_keys/private_key1.txt")

        self.rsa.encrypt(message, "text_files/public_keys/public_key1.txt")

        self.rsa.decrypt("text_files/encrypted_messages/encrypted_message1.txt", "text_files/private_keys/private_key1.txt")

        with open("text_files/decrypted_messages/decrypted_message1.txt", "r", encoding='utf-8') as f:
            decrypted_message = f.read()
            self.assertEqual(message, decrypted_message)

        self.rsa.sign(message, "text_files/private_keys/private_key1.txt")

        with open("text_files/public_keys/public_key1.txt", "r", encoding='utf-8') as f:
            e, n = map(int, f.read().splitlines())
        with open("text_files/signatures/signature1.txt", "r", encoding='utf-8') as f:
            signature = int(f.read())
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        verified = self.rsa.power_mod(signature, e, n) == h
        self.assertTrue(verified)

    def test_encryption_decryption_and_signature2(self):
        message = "ILOVESIMZIIS"
        self.rsa.save_keys("text_files/public_keys/public_key2.txt", "text_files/private_keys/private_key2.txt")

        self.rsa.encrypt(message, "text_files/public_keys/public_key2.txt")

        self.rsa.decrypt("text_files/encrypted_messages/encrypted_message2.txt", "text_files/private_keys/private_key2.txt")

        with open("text_files/decrypted_messages/decrypted_message2.txt", "r", encoding='utf-8') as f:
            decrypted_message = f.read()
            self.assertEqual(message, decrypted_message)

        self.rsa.sign(message, "text_files/private_keys/private_key2.txt")

        with open("text_files/public_keys/public_key2.txt", "r", encoding='utf-8') as f:
            e, n = map(int, f.read().splitlines())
        with open("text_files/signatures/signature2.txt", "r", encoding='utf-8') as f:
            signature = int(f.read())
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        verified = self.rsa.power_mod(signature, e, n) == h
        self.assertTrue(verified)

    def test_encryption_decryption_and_signature3(self):
        message = "qqqqqq"
        self.rsa.save_keys("text_files/public_keys/public_key3.txt", "text_files/private_keys/private_key3.txt")

        self.rsa.encrypt(message, "text_files/public_keys/public_key3.txt")

        self.rsa.decrypt("text_files/encrypted_messages/encrypted_message3.txt", "text_files/private_keys/private_key3.txt")

        with open("text_files/decrypted_messages/decrypted_message3.txt", "r", encoding='utf-8') as f:
            decrypted_message = f.read()
            self.assertEqual(message, decrypted_message)

        self.rsa.sign(message, "text_files/private_keys/private_key3.txt")

        with open("text_files/public_keys/public_key3.txt", "r", encoding='utf-8') as f:
            e, n = map(int, f.read().splitlines())
        with open("text_files/signatures/signature3.txt", "r", encoding='utf-8') as f:
            signature = int(f.read())
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        verified = self.rsa.power_mod(signature, e, n) == h
        self.assertTrue(verified)

    def test_encryption_decryption_and_signature4(self):
        message = "The sun was shining brightly in the clear blue sky, and the birds were singing their sweet melodies, while children played happily in the green park."
        self.rsa.save_keys("text_files/public_keys/public_key4.txt", "text_files/private_keys/private_key4.txt")

        self.rsa.encrypt(message, "text_files/public_keys/public_key4.txt")

        self.rsa.decrypt("text_files/encrypted_messages/encrypted_message4.txt", "text_files/private_keys/private_key4.txt")

        with open("text_files/decrypted_messages/decrypted_message4.txt", "r", encoding='utf-8') as f:
            decrypted_message = f.read()
            self.assertEqual(message, decrypted_message)

        self.rsa.sign(message, "text_files/private_keys/private_key4.txt")

        with open("text_files/public_keys/public_key4.txt", "r", encoding='utf-8') as f:
            e, n = map(int, f.read().splitlines())
        with open("text_files/signatures/signature4.txt", "r", encoding='utf-8') as f:
            signature = int(f.read())
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        verified = self.rsa.power_mod(signature, e, n) == h
        self.assertTrue(verified)

    def test_encryption_decryption_and_signature5(self):
        message = "Hi"
        self.rsa.save_keys("text_files/public_keys/public_key5.txt", "text_files/private_keys/private_key5.txt")

        self.rsa.encrypt(message, "text_files/public_keys/public_key5.txt")

        self.rsa.decrypt("text_files/encrypted_messages/encrypted_message5.txt", "text_files/private_keys/private_key5.txt")

        with open("text_files/decrypted_messages/decrypted_message5.txt", "r", encoding='utf-8') as f:
            decrypted_message = f.read()
            self.assertEqual(message, decrypted_message)

        self.rsa.sign(message, "text_files/private_keys/private_key5.txt")

        with open("text_files/public_keys/public_key5.txt", "r", encoding='utf-8') as f:
            e, n = map(int, f.read().splitlines())
        with open("text_files/signatures/signature5.txt", "r", encoding='utf-8') as f:
            signature = int(f.read())
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        verified = self.rsa.power_mod(signature, e, n) == h
        self.assertTrue(verified)

    def test_encryption_decryption_and_signature6(self):
        message = "Hello, world! 12345 @#$%^&*()"
        self.rsa.save_keys("text_files/public_keys/public_key6.txt", "text_files/private_keys/private_key6.txt")

        self.rsa.encrypt(message, "text_files/public_keys/public_key6.txt")

        self.rsa.decrypt("text_files/encrypted_messages/encrypted_message6.txt", "text_files/private_keys/private_key6.txt")

        with open("text_files/decrypted_messages/decrypted_message6.txt", "r", encoding='utf-8') as f:
            decrypted_message = f.read()
            self.assertEqual(message, decrypted_message)

        self.rsa.sign(message, "text_files/private_keys/private_key6.txt")

        with open("text_files/public_keys/public_key6.txt", "r", encoding='utf-8') as f:
            e, n = map(int, f.read().splitlines())
        with open("text_files/signatures/signature6.txt", "r", encoding='utf-8') as f:
            signature = int(f.read())
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        verified = self.rsa.power_mod(signature, e, n) == h
        self.assertTrue(verified)

    def test_encryption_decryption_and_signature7(self):
        message = "The formula for the area of a circle is (pi * r^2)"
        self.rsa.save_keys("text_files/public_keys/public_key7.txt", "text_files/private_keys/private_key7.txt")

        self.rsa.encrypt(message, "text_files/public_keys/public_key7.txt")

        self.rsa.decrypt("text_files/encrypted_messages/encrypted_message7.txt", "text_files/private_keys/private_key7.txt")

        with open("text_files/decrypted_messages/decrypted_message7.txt", "r", encoding='utf-8') as f:
            decrypted_message = f.read()
            self.assertEqual(message, decrypted_message)

        self.rsa.sign(message, "text_files/private_keys/private_key7.txt")

        with open("text_files/public_keys/public_key7.txt", "r", encoding='utf-8') as f:
            e, n = map(int, f.read().splitlines())
        with open("text_files/signatures/signature7.txt", "r", encoding='utf-8') as f:
            signature = int(f.read())
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        verified = self.rsa.power_mod(signature, e, n) == h
        self.assertTrue(verified)

    def test_encryption_decryption_and_signature8(self):
        message = "The sun was shining brightly in the clear blue sky, and the birds were singing their sweet melodies. Children played happily in the green park, while their parents watched them with smiles on their faces. The temperature was 25 degrees Celsius, and the time was 3:45 PM. It was a perfect day for a picnic"
        self.rsa.save_keys("text_files/public_keys/public_key8.txt", "text_files/private_keys/private_key8.txt")

        self.rsa.encrypt(message, "text_files/public_keys/public_key8.txt")

        self.rsa.decrypt("text_files/encrypted_messages/encrypted_message8.txt", "text_files/private_keys/private_key8.txt")

        with open("text_files/decrypted_messages/decrypted_message8.txt", "r", encoding='utf-8') as f:
            decrypted_message = f.read()
            self.assertEqual(message, decrypted_message)

        self.rsa.sign(message, "text_files/private_keys/private_key8.txt")

        with open("text_files/public_keys/public_key8.txt", "r", encoding='utf-8') as f:
            e, n = map(int, f.read().splitlines())
        with open("text_files/signatures/signature8.txt", "r", encoding='utf-8') as f:
            signature = int(f.read())
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        verified = self.rsa.power_mod(signature, e, n) == h
        self.assertTrue(verified)

    def test_encryption_decryption_and_signature9(self):
        message = "123333213122221111"
        self.rsa.save_keys("text_files/public_keys/public_key9.txt", "text_files/private_keys/private_key9.txt")

        self.rsa.encrypt(message, "text_files/public_keys/public_key9.txt")

        self.rsa.decrypt("text_files/encrypted_messages/encrypted_message9.txt", "text_files/private_keys/private_key9.txt")

        with open("text_files/decrypted_messages/decrypted_message9.txt", "r", encoding='utf-8') as f:
            decrypted_message = f.read()
            self.assertEqual(message, decrypted_message)

        self.rsa.sign(message, "text_files/private_keys/private_key9.txt")

        with open("text_files/public_keys/public_key9.txt", "r", encoding='utf-8') as f:
            e, n = map(int, f.read().splitlines())
        with open("text_files/signatures/signature9.txt", "r", encoding='utf-8') as f:
            signature = int(f.read())
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        verified = self.rsa.power_mod(signature, e, n) == h
        self.assertTrue(verified)

    def test_encryption_decryption_and_signature10(self):
        message = "@#Hello!"
        self.rsa.save_keys("text_files/public_keys/public_key0.txt", "text_files/private_keys/private_key0.txt")

        self.rsa.encrypt(message, "text_files/public_keys/public_key0.txt")

        self.rsa.decrypt("text_files/encrypted_messages/encrypted_message0.txt", "text_files/private_keys/private_key0.txt")

        with open("text_files/decrypted_messages/decrypted_message0.txt", "r", encoding='utf-8') as f:
            decrypted_message = f.read()
            self.assertEqual(message, decrypted_message)

        self.rsa.sign(message, "text_files/private_keys/private_key0.txt")

        with open("text_files/public_keys/public_key0.txt", "r", encoding='utf-8') as f:
            e, n = map(int, f.read().splitlines())
        with open("text_files/signatures/signature0.txt", "r", encoding='utf-8') as f:
            signature = int(f.read())
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
        verified = self.rsa.power_mod(signature, e, n) == h
        self.assertTrue(verified)


if __name__ == "__main__":
    unittest.main()
