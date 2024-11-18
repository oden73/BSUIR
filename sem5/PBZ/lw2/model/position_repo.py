from model.abstract_repository import AbstractRepository
from model.position import Position


class PositionRepository(AbstractRepository):
    def __init__(self) -> None:
        super().__init__()

    def select(self) -> list[Position]:
        query: str = "SELECT * FROM positions"

        result: list[tuple] = super().client.execute_with_output(query)
        positions_list: list[Position] = []
        for row in result:
            positions_list.append(Position(*row))

        return positions_list
