from model.department_repo import DepartmentRepository
from model.department import Department


class DepartmentController:
    def __init__(self) -> None:
        self.__repo: DepartmentRepository = DepartmentRepository()

    def select(self) -> list[tuple]:
        departments_list: list[Department] = self.__repo.select()

        result_list: list[tuple] = []
        for department in departments_list:
            result_list.append((str(department.id), department.name))

        return result_list
