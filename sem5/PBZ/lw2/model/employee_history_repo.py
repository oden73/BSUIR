from model.abstract_repository import AbstractRepository
from model.employee_history import EmployeeHistory


class EmployeeHistoryRepository(AbstractRepository):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, employee_id: str, department_id: str, position_id: str, tariff_rank: int, start_date: str,
               end_date: str) -> None:
        query: str = f"""
        INSERT INTO employee_history (employee_id, department_id, position_id, tariff_rank, start_date, end_date)
        VALUES ({employee_id}, {department_id}, {position_id}, {tariff_rank}, '{start_date}', '{end_date}');
        """

        super().client.execute_without_output(query)

    def update(self, ID: str, employee_id: str, department_id: str, position_id: str, tariff_rank: int, start_date: str,
               end_date: str) -> None:
        query: str = f"""
        UPDATE employee_history
        SET employee_id = {employee_id}, department_id = {department_id}, position_id = {position_id}, tariff_rank = {tariff_rank}, start_date = '{start_date}', end_date = '{end_date}'
        WHERE ID = {ID};
        """

        super().client.execute_without_output(query)

    def delete(self, ID: str) -> None:
        query: str = f"""
        DELETE FROM employee_history
        WHERE ID = {ID};        
        """

        super().client.execute_without_output(query)

    def select(self) -> list[EmployeeHistory]:
        query: str = "SELECT * FROM employee_history"

        result: list[tuple] = super().client.execute_with_output(query)
        employee_history_list: list[EmployeeHistory] = []
        for row in result:
            employee_history_list.append(EmployeeHistory(*row))

        return employee_history_list
