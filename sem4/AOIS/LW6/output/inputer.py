class Inputer:
    def __init__(self):
        pass

    @staticmethod
    def enter_operation_char() -> str:
        char: str = input()
        return char

    def enter_add_element(self) -> (str, str):
        ID: str = self.enter_ID()
        Pi: str = self.enter_Pi()
        return ID, Pi

    @staticmethod
    def enter_ID() -> str:
        ID: str = input()
        return ID

    @staticmethod
    def enter_Pi() -> str:
        Pi: str = input()
        return Pi
