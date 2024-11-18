from model.abstract_repository import AbstractRepository
from model.department import Department


class DepartmentRepository(AbstractRepository):
    def __init__(self) -> None:
        super().__init__()

    def select(self) -> list[Department]:
        query = "SELECT * FROM departments"

        result: list[tuple] = super().client.execute_with_output(query)
        departments_list: list[Department] = []
        for row in result:
            departments_list.append(Department(*row))

        return departments_list
