alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
            "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


class Cell:
    def __init__(self, ID: str = '', Pi: str = '', capacity: int = 2):
        self.ID: str = ID
        self.Pi: str = Pi
        self.V: int = self.generate_hash() if len(self.ID) >= 2 else 0
        self.h: int = 0
        self.generate_h(capacity)
        self.U: int = 0 if self.ID == '' and self.Pi == '' else 1
        self.next = None
        self.prev = None

    def generate_hash(self) -> int:
        return self.char_number(self.ID[0]) * 33 + self.char_number(self.ID[1])

    def generate_h(self, capacity):
        self.h = self.V % capacity


    @staticmethod
    def char_number(char: str) -> int:
        char = char.lower()
        return alphabet.index(char)

    def __bool__(self):
        return self.ID != '' and self.Pi != ''

    def __eq__(self, other):
        return self.ID == other.ID and self.Pi == other.Pi
