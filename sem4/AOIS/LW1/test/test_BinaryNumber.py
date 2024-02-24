import unittest
from BinaryNumber import BinaryNumber
from BinaryFixedPointNumber import BinaryFixedPointNumber


class TestBinaryNumber(unittest.TestCase):
    def test_number_init(self):
        self.number = BinaryNumber(12)
        self.assertEqual(self.number.number, [False, False, False, False, False, False, False, False, False,
                                              False, False, False, True, True, False, False])

    def test_add1(self):
        self.number1 = BinaryNumber(12)
        self.number2 = BinaryNumber(-3)
        self.result = self.number1 + self.number2
        self.answer = BinaryNumber(9)
        self.assertEqual(self.result.number, self.answer.number)

    def test_add2(self):
        self.number1 = BinaryNumber(10)
        self.number2 = BinaryNumber(-10)
        self.result = self.number1 + self.number2
        self.answer = BinaryNumber(0)
        self.assertEqual(self.result.number, self.answer.number)

    def test_add3(self):
        self.number1 = BinaryNumber(-12)
        self.number2 = BinaryNumber(-3)
        self.result = self.number1 + self.number2
        self.answer = BinaryNumber(-15)
        self.assertEqual(self.result.number, self.answer.number)

    def test_add4(self):
        self.number1 = BinaryNumber(0)
        self.number2 = BinaryNumber(-3)
        self.result = self.number1 + self.number2
        self.answer = BinaryNumber(-3)
        self.assertEqual(self.result.number, self.answer.number)

    def test_multiply1(self):
        self.number1 = BinaryNumber(7)
        self.number2 = BinaryNumber(5)
        self.result = self.number1 * self.number2
        self.answer = BinaryNumber(35)
        self.assertEqual(self.result.number, self.answer.number)

    def test_multiply2(self):
        self.number1 = BinaryNumber(7)
        self.number2 = BinaryNumber(0)
        self.result = self.number1 * self.number2
        self.answer = BinaryNumber(0)
        self.assertEqual(self.result.number, self.answer.number)

    def test_multiply3(self):
        self.number1 = BinaryNumber(2)
        self.number2 = BinaryNumber(-5)
        self.result = self.number1 * self.number2
        self.answer = BinaryNumber(-10)
        self.assertEqual(self.result.number, self.answer.number)

    def test_multiply4(self):
        self.number1 = BinaryNumber(-2)
        self.number2 = BinaryNumber(-3)
        self.result = self.number1 * self.number2
        self.answer = BinaryNumber(6)
        self.assertEqual(self.result.number, self.answer.number)

    def test_division1(self):
        self.number1 = BinaryNumber(4)
        self.number2 = BinaryNumber(2)
        self.result = self.number1 / self.number2
        self.answer = '[0]10.00000'
        self.assertEqual(self.result.__str__(), self.answer)

    def test_division2(self):
        self.number1 = BinaryNumber(-6)
        self.number2 = BinaryNumber(2)
        self.result = self.number1 / self.number2
        self.answer = '[1]11.00000'
        self.assertEqual(self.result.__str__(), self.answer)

    def test_division3(self):
        self.number1 = BinaryNumber(16)
        self.number2 = BinaryNumber(-7)
        self.result = self.number1 / self.number2
        self.answer = '[1]10.01001'
        self.assertEqual(self.result.__str__(), self.answer)

    def test_division4(self):
        self.number1 = BinaryNumber(-3)
        self.number2 = BinaryNumber(-6)
        self.result = self.number1 / self.number2
        self.answer = '[0]0.10000'
        self.assertEqual(self.result.__str__(), self.answer)


if __name__ == "__main__":
    unittest.main()
