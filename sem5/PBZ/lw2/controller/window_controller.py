from view.add_employee_window import AddEmployeeWindow
from view.edit_employee_window import EditEmployeeWindow
from view.delete_employee_window import DeleteEmployeeWindow

from view.add_employee_history_window import AddEmployeeHistoryWindow
from view.edit_employee_history_window import EditEmployeeHistoryWindow
from view.delete_employee_history_window import DeleteEmployeeHistoryWindow

from view.query_employees_by_position_and_age_window import QueryEmployeesByPositionAndAgeWindow
from view.query_staffing_window import QueryStaffingWindow
from view.query_employees_by_age_window import QueryEmployeesByAgeWindow


class WindowController:
    def __init__(self) -> None:
        pass

    def add_employee(self):
        AddEmployeeWindow()

    def edit_employee(self):
        EditEmployeeWindow()

    def delete_employee(self):
        DeleteEmployeeWindow()

    def add_employee_history(self):
        AddEmployeeHistoryWindow()

    def edit_employee_history(self):
        EditEmployeeHistoryWindow()

    def delete_employee_history(self):
        DeleteEmployeeHistoryWindow()

    def query_staffing(self):
        QueryStaffingWindow()

    def query_employees_by_age(self):
        QueryEmployeesByAgeWindow()

    def query_employees_by_position_and_age(self):
        QueryEmployeesByPositionAndAgeWindow()
