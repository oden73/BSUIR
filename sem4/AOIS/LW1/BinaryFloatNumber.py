from math import modf


class BinaryFloatNumber:
    def __init__(self, value=0.0):
        self.__exponent_const, self.__exponent_degree, self.__exponent_bits, self.__mantissa_bits = (127, 127, 8, 23)
        self.__sign_bit, self.__exponent, self.__mantissa = (False if value >= 0 else True, [], [])
        value = abs(value)
        float_part, int_part = (modf(value)[0], int(modf(value)[1]))
        int_binary, float_binary = (convert_to_binary(int_part), convert_to_binary(float_part))
        temp_mantissa, self.__exponent_degree = form_temp_mantissa(int_binary, float_binary, self.__exponent_const)
        extra_zeros = []
        for i in range(0, self.__mantissa_bits - len(temp_mantissa)):
            extra_zeros.append(False)
        self.__mantissa = temp_mantissa + extra_zeros
        self.__exponent = convert_to_binary(self.__exponent_degree)
        if len(self.__exponent) < self.__exponent_bits:
            for i in range(0, self.__exponent_bits - len(self.__exponent)):
                self.__exponent.insert(0, False)

    def __str__(self):
        return str(int(self.__sign_bit)) + ' ' + list_print(self.__exponent) + ' ' + list_print(self.__mantissa)

    def __add__(self, other):
        current_mantissa, other_mantissa = (mantissa_fixing(self.mantissa, self.exponent),
                                            mantissa_fixing(other.mantissa, other.exponent))
        current_exponent, other_exponent = (self.exponent, other.exponent)
        new_exponent = current_exponent
        new_exponent_degree = max(self.exponent_degree, other.exponent_degree)
        if self.exponent_degree < other.exponent_degree:
            new_exponent = other_exponent
            current_mantissa = mantissa_shift(current_mantissa, other.exponent_degree - self.exponent_degree)
        elif self.exponent_degree > other.exponent_degree:
            other_mantissa = mantissa_shift(other_mantissa, self.exponent_degree - other.exponent_degree)
        new_mantissa = mantissa_addition(current_mantissa, other_mantissa)
        if len(new_mantissa) == 24:
            new_mantissa = new_mantissa[1:]
        elif len(new_mantissa) == 25:
            exponent_fixing(new_exponent)
            new_mantissa = new_mantissa[1:24]
        result = BinaryFloatNumber()
        result.exponent = new_exponent
        result.exponent_degree = new_exponent_degree
        result.mantissa = new_mantissa[len(new_mantissa) - self.__mantissa_bits:]
        return result

    def decimal_view(self):
        float_part = 0
        for i in range(0, self.__mantissa_bits):
            float_part += pow(2, -(i + 1)) * int(self.mantissa[i])
        float_part += 1
        return pow(-1, int(self.__sign_bit)) * float_part * pow(2, (self.exponent_degree - self.__exponent_const))

    @property
    def exponent(self):
        return self.__exponent

    @property
    def mantissa(self):
        return self.__mantissa

    @property
    def exponent_degree(self):
        return self.__exponent_degree

    @exponent.setter
    def exponent(self, new_exponent):
        if len(new_exponent) != self.__exponent_bits:
            raise ValueError('неверный формат экспоненты')
        self.__exponent = new_exponent

    @mantissa.setter
    def mantissa(self, new_mantissa):
        if len(new_mantissa) != self.__mantissa_bits:
            raise ValueError('неверный формат мантиссы')
        self.__mantissa = new_mantissa

    @exponent_degree.setter
    def exponent_degree(self, degree):
        self.__exponent_degree = degree


def convert_to_binary(value):
    binary = []
    if value < 1:
        operations = 0
        while value != 0 and operations < 22:
            value *= 2
            binary.append(bool(int(value // 1)))
            value %= 1
            operations += 1
        return binary
    while value > 0:
        binary.insert(0, bool(value % 2))
        value //= 2
    return binary


def list_print(current_list):
    out = ''
    for i in current_list:
        out += str(int(i))
    return out


def form_temp_mantissa(int_binary, float_binary, exponent_const):
    if len(int_binary) == 0:
        if len(float_binary) == 0:
            return [], exponent_const
        non_zero = 0
        while not float_binary[non_zero]:
            non_zero += 1
        return float_binary[non_zero + 1:], exponent_const - non_zero - 1
    else:
        return int_binary[1:] + float_binary, exponent_const + len(int_binary) - 1


def mantissa_shift(mantissa, shift):
    new_mantissa = []
    for i in range(0, shift):
        new_mantissa.append(False)
    for i in range(0, len(mantissa) - shift):
        new_mantissa.append(mantissa[i])
    return new_mantissa


def mantissa_addition(current_mantissa, other_mantissa):
    new_mantissa = []
    adding = False
    for i in range(len(current_mantissa) - 1, -1, -1):
        value = int(current_mantissa[i]) + int(other_mantissa[i]) + int(adding)
        new_mantissa.insert(0, bool(value % 2))
        adding = bool(value // 2)
    if adding:
        new_mantissa.insert(0, True)
    return new_mantissa


def exponent_fixing(exponent):
    position = len(exponent) - 1
    while exponent[position]:
        if position == -1:
            raise ValueError('переполнение экспоненты')
        exponent[position] = False
        position -= 1
    exponent[position] = True
    return exponent


def mantissa_fixing(mantissa, exponent):
    if list_print(mantissa) == '00000000000000000000000' and list_print(exponent) == '01111111':
        return [False] + mantissa
    else:
        return [True] + mantissa
