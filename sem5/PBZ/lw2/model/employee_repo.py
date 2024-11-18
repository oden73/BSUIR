from model.abstract_repository import AbstractRepository
from model.employee import Employee


class EmployeesRepository(AbstractRepository):
    def __init__(self):
        super().__init__()

    def insert(self, name: str, age: str, gender: str, marital_status: str) -> None:
        query: str = f"""
        INSERT INTO employees (name, age, gender, marital_status)
        VALUES ("{name}", {age}, "{gender}", "{marital_status}");
        """

        print(query)

        super().client.execute_without_output(query)

    def update(self, ID: str, name: str, age: str, gender: str, marital_status: str) -> None:
        query: str = f"""
        UPDATE employees
        SET name = "{name}", age = {age}, gender = "{gender}", marital_status = "{marital_status}"
        WHERE ID = {ID};
        """

        super().client.execute_without_output(query)

    def delete(self, ID: str) -> None:
        query: str = f"""
        DELETE FROM employees
        WHERE ID = {ID};
        """

        super().client.execute_without_output(query)

    def select(self) -> list[Employee]:
        query: str = "SELECT * FROM employees"

        result: list[tuple] = super().client.execute_with_output(query)
        employee_list: list[Employee] = []
        for row in result:
            employee_list.append(Employee(*row))

        return employee_list
