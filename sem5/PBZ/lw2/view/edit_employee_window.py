import tkinter as tk
from tkinter import messagebox

from controller.employee_controller import EmployeeController


class EditEmployeeWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.__controller: EmployeeController = EmployeeController()

        self.title("Edit Employee")
        tk.Label(self, text="Enter Employee ID").grid(row=0, column=0)
        self.employee_id_entry = tk.Entry(self)
        self.employee_id_entry.grid(row=0, column=1)

        tk.Label(self, text="Enter New Employee Name").grid(row=1, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self, text="Enter New Employee Age").grid(row=2, column=0)
        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=2, column=1)

        tk.Label(self, text="Enter New Employee Gender").grid(row=3, column=0)
        self.gender_entry = tk.Entry(self)
        self.gender_entry.grid(row=3, column=1)

        tk.Label(self, text="Enter New Employee Marital Status").grid(row=4, column=0)
        self.marital_status_entry = tk.Entry(self)
        self.marital_status_entry.grid(row=4, column=1)

        tk.Button(self, text="Submit", command=self.submit).grid(row=5, column=0, columnspan=2)

    def submit(self):
        employee_id = self.employee_id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        marital_status = self.marital_status_entry.get()
        if employee_id and name and age and gender and marital_status:
            self.__controller.update(employee_id, name, age, gender, marital_status)
            messagebox.showinfo("Success", "Employee history added successfully")
            self.destroy()
