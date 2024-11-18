from model.employee_repo import EmployeesRepository
from model.employee import Employee


class EmployeeController:
    def __init__(self) -> None:
        self.__repo: EmployeesRepository = EmployeesRepository()

    def insert(self, name: str, age: str, gender: str, marital_status: str) -> None:
        self.__repo.insert(name, age, gender, marital_status)

    def update(self, ID: str, name: str, age: str, gender: str, marital_status: str) -> None:
        self.__repo.update(ID, name, age, gender, marital_status)

    def delete(self, ID: str) -> None:
        self.__repo.delete(ID)

    def select(self) -> list[tuple]:
        employee_list: list[Employee] = self.__repo.select()

        result_list: list[tuple] = []
        for employee in employee_list:
            result_list.append((str(employee.id), employee.name, str(employee.age), employee.gender,
                                employee.marital_status))

        return result_list
