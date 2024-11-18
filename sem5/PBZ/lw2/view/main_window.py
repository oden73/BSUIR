import tkinter as tk
from tkinter import ttk

from controller.window_controller import WindowController
from controller.employee_controller import EmployeeController
from controller.department_controller import DepartmentController
from controller.position_controller import PositionController
from controller.staffing_controller import StaffingController
from controller.employee_history_controller import EmployeeHistoryController


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.__window_controller: WindowController = WindowController()
        self.__employee_controller: EmployeeController = EmployeeController()
        self.__department_controller: DepartmentController = DepartmentController()
        self.__position_controller: PositionController = PositionController()
        self.__staffing_controller: StaffingController = StaffingController()
        self.__employee_history_controller: EmployeeHistoryController = EmployeeHistoryController()

        self.title("Database Viewer")
        self.geometry("800x600")

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(fill=tk.X)
        self.buttons = [
            tk.Button(self.button_frame, text="Employees", command=self.show_employees),
            tk.Button(self.button_frame, text="Departments", command=self.show_departments),
            tk.Button(self.button_frame, text="Positions", command=self.show_positions),
            tk.Button(self.button_frame, text="Staffing", command=self.show_staffing),
            tk.Button(self.button_frame, text="Employee History", command=self.show_employee_history)
        ]

        for button in self.buttons:
            button.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.employee_button_frame = tk.Frame(self)
        self.employee_button_frame.pack(fill=tk.X)
        self.employee_buttons = [
            tk.Button(self.employee_button_frame, text="Add Employee",
                      command=self.__window_controller.add_employee),
            tk.Button(self.employee_button_frame, text="Edit Employee",
                      command=self.__window_controller.edit_employee),
            tk.Button(self.employee_button_frame, text="Delete Employee",
                      command=self.__window_controller.delete_employee)
        ]

        for button in self.employee_buttons:
            button.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.history_button_frame = tk.Frame(self)
        self.history_button_frame.pack(fill=tk.X)
        self.history_buttons = [
            tk.Button(self.history_button_frame, text="Add Employee History",
                      command=self.__window_controller.add_employee_history),
            tk.Button(self.history_button_frame, text="Edit Employee History",
                      command=self.__window_controller.edit_employee_history),
            tk.Button(self.history_button_frame, text="Delete Employee History",
                      command=self.__window_controller.delete_employee_history)
        ]

        for button in self.history_buttons:
            button.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.query_button_frame = tk.Frame(self)
        self.query_button_frame.pack(fill=tk.X)
        self.query_buttons = [
            tk.Button(self.query_button_frame, text="Department Staffing",
                      command=self.__window_controller.query_staffing),
            tk.Button(self.query_button_frame, text="Female Employees Over 55",
                      command=self.__window_controller.query_employees_by_age),
            tk.Button(self.query_button_frame, text="Employees Under Specified Age on Specified Position",
                      command=self.__window_controller.query_employees_by_position_and_age)
        ]
        for button in self.query_buttons:
            button.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Таблица
        self.tree = ttk.Treeview(self)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Начальная таблица
        self.show_employees()

    def show_employees(self):
        self.tree.delete(*self.tree.get_children())
        self.tree['columns'] = ('ID', 'Name', 'Age', 'Gender', 'Marital Status')
        self.tree.column("#0", width=0, stretch=tk.NO)
        for column in self.tree['columns']:
            self.tree.column(column, anchor=tk.W, width=100)
            self.tree.heading(column, text=column, anchor=tk.W)

        rows = self.__employee_controller.select()
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def show_departments(self):
        self.tree.delete(*self.tree.get_children())
        self.tree['columns'] = ('ID', 'Name')
        self.tree.column("#0", width=0, stretch=tk.NO)
        for column in self.tree['columns']:
            self.tree.column(column, anchor=tk.W, width=100)
            self.tree.heading(column, text=column, anchor=tk.W)

        rows = self.__department_controller.select()
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def show_positions(self):
        self.tree.delete(*self.tree.get_children())
        self.tree['columns'] = ('ID', 'Name', 'Short Name', 'Code', 'Lower Tariff Rank', 'Upper Tariff Rank')
        self.tree.column("#0", width=0, stretch=tk.NO)
        for column in self.tree['columns']:
            self.tree.column(column, anchor=tk.W, width=100)
            self.tree.heading(column, text=column, anchor=tk.W)

        rows = self.__position_controller.select()
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def show_staffing(self):
        self.tree.delete(*self.tree.get_children())
        self.tree['columns'] = ('ID', 'Department ID', 'Position ID', 'Quantity')
        self.tree.column("#0", width=0, stretch=tk.NO)
        for column in self.tree['columns']:
            self.tree.column(column, anchor=tk.W, width=100)
            self.tree.heading(column, text=column, anchor=tk.W)
        rows = self.__staffing_controller.select()
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def show_employee_history(self):
        self.tree.delete(*self.tree.get_children())
        self.tree['columns'] = (
        'ID', 'Employee ID', 'Department ID', 'Position ID', 'Tariff Rank', 'Start Date', 'End Date')
        self.tree.column("#0", width=0, stretch=tk.NO)
        for column in self.tree['columns']:
            self.tree.column(column, anchor=tk.W, width=100)
            self.tree.heading(column, text=column, anchor=tk.W)
        rows = self.__employee_history_controller.select()
        for row in rows:
            self.tree.insert('', 'end', values=row)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
