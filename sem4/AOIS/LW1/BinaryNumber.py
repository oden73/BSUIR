from BinaryFixedPointNumber import BinaryFixedPointNumber


class BinaryNumber:
    def __init__(self, value=0):
        if value < -(pow(2, 15) - 1) or value > pow(2, 15) - 1:
            raise ValueError("некорректное число")
        self.__number = []
        for i in range(0, 16):
            self.__number.append(False)
        self.__bit_maximum = 15
        self.__number[0] = False if value >= 0 else True
        value = abs(value)
        list_position = 15
        while value > 0:
            self.__number[list_position] = (bool(value % 2))
            value //= 2
            list_position -= 1

    def __str__(self):
        print_string = '['
        print_string += str(int(self.__number[0]))
        print_string += ']'
        for i in range(1, len(self.__number)):
            print_string += str(int(self.__number[i]))
        return print_string

    def __add__(self, other):
        current_list = self.additional_view().number
        other_list = other.number
        if other_list[0]:
            other_list = other.additional_view().number
        result_list = []
        for i in range(0, 16):
            result_list.append(False)
        adding = False
        for i in range(15, -1, -1):
            value = int(current_list[i]) + int(other_list[i]) + int(adding)
            result_list[i] = bool(value % 2)
            adding = bool(value // 2)
        result = BinaryNumber()
        result.number = result_list
        if result_list[0]:
            back_reverse_list = getting_addition_answer(result_list)
            result.number = back_reverse_list
        return result

    def __sub__(self, other):
        negative_other = BinaryNumber()
        negative_other_list = other.number
        negative_other_list[0] = 1 - negative_other_list[0]
        negative_other.number = negative_other_list
        return self + negative_other

    def __mul__(self, other):
        result = BinaryNumber()
        result_list = []
        for i in range(0, 30):
            result_list.append(False)
        multiplying_list = self.__multiplying(other)
        adding = 0
        for i in range(29, -1, -1):
            value = 0
            for j in range(len(multiplying_list) - 1, -1, -1):
                value += int(multiplying_list[j][i])
            value += adding
            result_list[i] = bool(value % 2)
            adding = value // 2
        result_list = result_list[14:]
        result_list[0] = bool((int(self.__number[0]) + int(other.number[0])) % 2)
        result.number = result_list
        return result

    def __truediv__(self, other):
        if other.number == BinaryNumber().number:
            raise ZeroDivisionError('деление на 0')
        current_list, other_list = (remove_extra_zeros(self.__number[1::]), remove_extra_zeros(other.number[1::]))
        (subtrahend, result_list) = (current_list[0:len(other_list)], [])
        (end, dot_index, after_dot) = (len(other_list) - 1, -1, 0)
        subtrahend, result_list, dot_index, end = initial_fixing(subtrahend, current_list, other_list, result_list,
                                                                 dot_index, end)
        while True:
            if sub_number_compare(subtrahend, other_list):
                subtrahend, result_list, dot_index, after_dot, end = subtraction(subtrahend, current_list, other_list,
                                                                                 result_list, dot_index, after_dot, end)
            else:
                subtrahend, result_list, dot_index, after_dot, end = adding_to_subtrahend(subtrahend, current_list,
                                                                                          result_list, dot_index,
                                                                                          after_dot, end)
            if after_dot >= 5:
                break
        return self.__form_div_answer(other, dot_index, result_list)

    def __multiplying(self, other):
        current_list = self.__number[1:]
        other_list = other.number[1:]
        multiplying_list = []
        for i in range(0, len(other_list)):
            temp_multiplying_list = []
            for j in range(0, 30):
                temp_multiplying_list.append(False)
            multiplying_list.append(temp_multiplying_list)
        for i in range(14, -1, -1):
            if other_list[i]:
                for j in range(len(multiplying_list[i]) - (14 - i) - 1, len(multiplying_list[i]) - 14 - (14 - i) - 1,
                               -1):
                    multiplying_list[14 - i][j] = current_list[14 - (len(multiplying_list[i]) - 14 + i - 1 - j)]
        return multiplying_list

    def __form_div_answer(self, other, dot_index, result_list):
        number = [bool((int(self.__number[0]) + int(other.number[0])) % 2)]
        number += result_list
        return BinaryFixedPointNumber(number, dot_index + 1)

    def increment(self):
        position = 15
        while self.__number[position]:
            self.__number[position] = False
            position -= 1
        self.__number[position] = True

    def reverse_view(self):
        if not self.__number[0]:
            return self
        reverse_view_list = [self.__number[0]]
        for i in range(1, len(self.__number)):
            reverse_view_list.append(bool(1 - int(self.__number[i])))
        reverse_view_number = BinaryNumber()
        reverse_view_number.number = reverse_view_list
        return reverse_view_number

    def additional_view(self):
        if not self.__number[0]:
            return self
        additional_view_list = self.reverse_view().number
        additional_view_number = BinaryNumber()
        additional_view_number.number = additional_view_list
        additional_view_number.increment()
        return additional_view_number

    def decimal_view(self):
        value = 0
        for i in range(15, 0, -1):
            value += int(self.__number[i]) * pow(2, 15 - i)
        return value if not self.__number[0] else -value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        if len(new_number) > 16:
            raise ValueError("некорректное число")
        self.__number = new_number


def getting_addition_answer(result_list):
    back_reverse_list = []
    for i in range(0, 16):
        back_reverse_list.append(False)
    for i in range(1, 16):
        back_reverse_list[i] = bool(1 - int(result_list[i]))
    back_reverse_number = BinaryNumber()
    back_reverse_number.number = back_reverse_list
    back_reverse_number.increment()
    back_reverse_list = back_reverse_number.number
    back_reverse_list[0] = True
    return back_reverse_list


def sub_number_compare(current_list, other_list):
    current, other = 0, 0
    for i in range(len(current_list) - 1, -1, -1):
        current += pow(2, len(current_list) - i - 1) * int(current_list[i])
    for i in range(len(other_list) - 1, -1, -1):
        other += pow(2, len(other_list) - i - 1) * int(other_list[i])
    return current >= other


def column_subtraction(subtrahend, other_list):
    sub_result = []
    for i in range(len(subtrahend) - 1, -1, -1):
        if int(subtrahend[i]) >= int(other_list[i]):
            sub_result.insert(0, bool(int(subtrahend[i]) - int(other_list[i])))
        else:
            position = i
            while not subtrahend[position]:
                subtrahend[position] = True
                position -= 1
            subtrahend[position] = False
            sub_result.append(True)
    return sub_result


def subtraction(subtrahend, current_list, other_list, result_list, dot_index, after_dot, end):
    if len(subtrahend) > len(other_list):
        other_list.insert(0, False)
    sub_result = column_subtraction(subtrahend, other_list)
    non_zero_index = len(sub_result)
    for i in range(0, len(sub_result)):
        if sub_result[i]:
            non_zero_index = i
            break
    subtrahend = sub_result[non_zero_index:len(sub_result)]
    result_list.append(True)
    if not other_list[0]:
        other_list.pop(0)
    if dot_index != -1:
        after_dot += 1
    if end < len(current_list) - 1:
        end += 1
        subtrahend.append(current_list[end])
    elif end == len(current_list) - 1:
        dot_index = len(result_list)
        end += 1
        subtrahend.append(False)
    else:
        subtrahend.append(False)
    return subtrahend, result_list, dot_index, after_dot, end


def adding_to_subtrahend(subtrahend, current_list, result_list, dot_index, after_dot, end):
    result_list.append(False)
    if end > len(current_list) - 1:
        after_dot += 1
        subtrahend.append(False)
    elif end == len(current_list) - 1:
        dot_index = len(result_list)
        end += 1
        subtrahend.append(False)
    else:
        end += 1
        subtrahend.append(current_list[end])
    return subtrahend, result_list, dot_index, after_dot, end


def remove_extra_zeros(current_list):
    while not current_list[0]:
        current_list.pop(0)
    return current_list


def initial_fixing(subtrahend, current_list, other_list, result_list, dot_index, end):
    if not sub_number_compare(subtrahend, other_list):
        if end >= len(current_list) - 1:
            result_list.append(False)
            subtrahend.append(False)
            dot_index = 1
        else:
            end += 1
            subtrahend.append(current_list[end])
    return subtrahend, result_list, dot_index, end
