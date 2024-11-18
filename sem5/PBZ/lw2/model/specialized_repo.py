from model.abstract_repository import AbstractRepository


class SpecializedRepository(AbstractRepository):
    def __init__(self) -> None:
        super().__init__()

    def staffing_schedule(self, department_id: str) -> list[tuple]:
        query: str = f"""
        SELECT p.name AS position_name, p.short_name, p.code, p.lower_tariff_rank, p.upper_tariff_rank, s.quantity
        FROM staffing s
        JOIN positions p ON s.position_id = p.ID
        WHERE s.department_id = {department_id};
        """

        result: list[tuple] = super().client.execute_with_output(query)
        return result

    def female_employee_list(self) -> list[tuple]:
        query: str = """
        SELECT e.name AS fio, e.gender, d.name AS department_name
        FROM employees e
        JOIN employee_history eh ON e.ID = eh.employee_id
        JOIN departments d ON eh.department_id = d.ID
        WHERE e.gender = 'Female' AND e.age >= 55;
        """

        result: list[tuple] = super().client.execute_with_output(query)
        return result

    def special_employee_list(self, position_id: str, age_boarder: str) -> list[tuple]:
        query: str = f"""
        SELECT e.name, e.age, d.name AS department_name, p.name AS position_name
        FROM employees e
        JOIN employee_history eh ON e.ID = eh.employee_id
        JOIN departments d ON eh.department_id = d.ID
        JOIN positions p ON eh.position_id = p.ID
        WHERE eh.position_id = {position_id} AND e.age < {age_boarder};
        """

        result: list[tuple] = super().client.execute_with_output(query)
        return result
