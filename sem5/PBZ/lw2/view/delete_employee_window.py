import tkinter as tk
from tkinter import messagebox

from controller.employee_controller import EmployeeController


class DeleteEmployeeWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.__controller: EmployeeController = EmployeeController()

        self.title("Delete Employee")
        tk.Label(self, text="Enter Employee ID").grid(row=0, column=0)
        self.employee_id_entry = tk.Entry(self)
        self.employee_id_entry.grid(row=0, column=1)

        tk.Button(self, text="Submit", command=self.submit).grid(row=1, column=0, columnspan=2)

    def submit(self):
        employee_id = self.employee_id_entry.get()
        if employee_id:
            self.__controller.delete(employee_id)
            messagebox.showinfo("Success", "Employee deleted successfully")
            self.destroy()
