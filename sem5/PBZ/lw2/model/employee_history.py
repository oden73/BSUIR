from datetime import date


class EmployeeHistory:
    def __init__(self, id: int, employee_id: int, department_id: int, position_id: int, tariff_rank: int, start_date: date,
                 end_date: date) -> None:
        self.id: int = id
        self.employee_id: int = employee_id
        self.department_id: int = department_id
        self.position_id: int = position_id
        self.tariff_rank: int = tariff_rank
        self.start_date: date = start_date
        self.end_date: date = end_date
