from model.position_repo import PositionRepository
from model.position import Position


class PositionController:
    def __init__(self) -> None:
        self.__repo: PositionRepository = PositionRepository()

    def select(self) -> list[tuple]:
        position_list: list[Position] = self.__repo.select()

        result_list: list[tuple] = []
        for position in position_list:
            result_list.append((str(position.id), position.name, position.short_name, position.code,
                                str(position.lower_tariff_rank), str(position.upper_tariff_rank)))

        return result_list
