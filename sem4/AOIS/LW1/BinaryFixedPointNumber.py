from BinaryFloatNumber import list_print


class BinaryFixedPointNumber:
    def __init__(self, number, dot_index):
        self.__int_part, self.__float_part = (number[:dot_index], number[dot_index:])
        if len(self.__int_part) == 1:
            self.__int_part.append(False)

    def __str__(self):
        return ('[' + str(int(self.__int_part[0])) + ']' + list_print(self.__int_part[1:]) + '.' +
                list_print(self.__float_part))

    def decimal_view(self):
        int_part, float_part = 0, 0
        for i in range(0, len(self.__int_part)):
            int_part += pow(2, len(self.__int_part) - 1 - i) * int(self.__int_part[i])
        for i in range(0, len(self.__float_part)):
            float_part += pow(2, -(i + 1)) * int(self.__float_part[i])
        return int_part + float_part
