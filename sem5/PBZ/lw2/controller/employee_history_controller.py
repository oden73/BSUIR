from model.employee_history_repo import EmployeeHistoryRepository
from model.employee_history import EmployeeHistory


class EmployeeHistoryController:
    def __init__(self) -> None:
        self.__repo: EmployeeHistoryRepository = EmployeeHistoryRepository()

    def insert(self, employee_id: str, department_id: str, position_id: str, tariff_rank: int, start_date: str,
               end_date: str) -> None:
        self.__repo.insert(employee_id, department_id, position_id, tariff_rank, start_date, end_date)

    def update(self, ID: str, employee_id: str, department_id: str, position_id: str, tariff_rank: int, start_date: str,
               end_date: str) -> None:
        self.__repo.update(ID, employee_id, department_id, position_id, tariff_rank, start_date, end_date)

    def delete(self, ID: str) -> None:
        self.__repo.delete(ID)

    def select(self) -> list[tuple]:
        employee_history_list: list[EmployeeHistory] = self.__repo.select()

        result_list: list[tuple] = []
        for eh in employee_history_list:
            result_list.append((str(eh.id), str(eh.employee_id), str(eh.department_id), str(eh.position_id),
                                str(eh.tariff_rank), str(eh.start_date), str(eh.end_date)))

        return result_list
