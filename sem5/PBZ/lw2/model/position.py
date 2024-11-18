class Position:
    def __init__(self, id: int, name: str, short_name: str, code: str, lower_tariff_rank: int, upper_tariff_rank: int) \
            -> None:
        self.id: int = id
        self.name: str = name
        self.short_name: str = short_name
        self.code: str = code
        self.lower_tariff_rank: int = lower_tariff_rank
        self.upper_tariff_rank: int = upper_tariff_rank
