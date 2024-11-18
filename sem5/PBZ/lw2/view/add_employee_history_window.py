import tkinter as tk
from tkinter import messagebox

from controller.employee_history_controller import EmployeeHistoryController


class AddEmployeeHistoryWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.__controller: EmployeeHistoryController = EmployeeHistoryController()

        self.title("Add Employee History")
        tk.Label(self, text="Enter Employee ID").grid(row=0, column=0)
        self.employee_id_entry = tk.Entry(self)
        self.employee_id_entry.grid(row=0, column=1)

        tk.Label(self, text="Enter Department ID").grid(row=1, column=0)
        self.department_id_entry = tk.Entry(self)
        self.department_id_entry.grid(row=1, column=1)

        tk.Label(self, text="Enter Position ID").grid(row=2, column=0)
        self.position_id_entry = tk.Entry(self)
        self.position_id_entry.grid(row=2, column=1)

        tk.Label(self, text="Enter Tariff Rank").grid(row=3, column=0)
        self.tariff_rank_entry = tk.Entry(self)
        self.tariff_rank_entry.grid(row=3, column=1)

        tk.Label(self, text="Enter Start Date (YYYY-MM-DD)").grid(row=4, column=0)
        self.start_date_entry = tk.Entry(self)
        self.start_date_entry.grid(row=4, column=1)

        tk.Label(self, text="Enter End Date (YYYY-MM-DD)").grid(row=5, column=0)
        self.end_date_entry = tk.Entry(self)
        self.end_date_entry.grid(row=5, column=1)

        tk.Button(self, text="Submit", command=self.submit).grid(row=6, column=0, columnspan=2)

    def submit(self):
        employee_id = self.employee_id_entry.get()
        department_id = self.department_id_entry.get()
        position_id = self.position_id_entry.get()
        tariff_rank = self.tariff_rank_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        if employee_id and department_id and position_id and tariff_rank and start_date and end_date:
            self.__controller.insert(employee_id, department_id, position_id, int(tariff_rank), start_date, end_date)
            messagebox.showinfo("Success", "Employee history added successfully")
            self.destroy()
