from model.abstract_repository import AbstractRepository
from model.staffing import Staffing


class StaffingRepository(AbstractRepository):
    def __init__(self) -> None:
        super().__init__()

    def select(self) -> list[Staffing]:
        query: str = "SELECT * FROM staffing"

        result: list[tuple] = super().client.execute_with_output(query)
        staffing_list: list[Staffing] = []
        for row in result:
            staffing_list.append(Staffing(*row))

        return staffing_list
