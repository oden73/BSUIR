class Inputer:
    def __init__(self):
        pass

    @staticmethod
    def enter_operation_key() -> str:
        key: str = input()
        return key

    @staticmethod
    def enter_index() -> int:
        index: int = int(input())
        return index

    @staticmethod
    def enter_string() -> str:
        string: str = input()
        return string
