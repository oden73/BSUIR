class LogicalFunctions:
    def __init__(self):
        pass

    def return_value(self, function_string, value1, value2) -> int:
        match function_string:
            case 'f4':
                return self.prohibition_of_second_argument(value1, value2)
            case 'f6':
                return self.disparity(value1, value2)
            case 'f9':
                return self.equivalence(value1, value2)
            case 'f11':
                return self.implication(value1, value2)

    @staticmethod
    def prohibition_of_second_argument(value1, value2) -> int:
        return int(not bool(value1) and bool(value2))

    def disparity(self, value1, value2) -> int:
        return int(bool(self.prohibition_of_second_argument(value1, value2)) or
                   bool(self.prohibition_of_second_argument(value2, value1)))

    @staticmethod
    def equivalence(value1, value2) -> int:
        return int((bool(value1) and bool(value2)) or (not bool(value1) and not bool(value2)))

    @staticmethod
    def implication(value1, value2) -> int:
        return int(bool(value1) or not bool(value2))
