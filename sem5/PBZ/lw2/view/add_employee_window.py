import tkinter as tk
from tkinter import messagebox

from controller.employee_controller import EmployeeController


class AddEmployeeWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.__controller: EmployeeController = EmployeeController()

        self.title("Add Employee")
        tk.Label(self, text="Enter Employee Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self, text="Enter Employee Age").grid(row=1, column=0)
        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=1, column=1)

        tk.Label(self, text="Enter Employee Gender").grid(row=2, column=0)
        self.gender_entry = tk.Entry(self)
        self.gender_entry.grid(row=2, column=1)

        tk.Label(self, text="Enter Employee Marital Status").grid(row=3, column=0)
        self.marital_status_entry = tk.Entry(self)
        self.marital_status_entry.grid(row=3, column=1)

        tk.Button(self, text="Submit", command=self.submit).grid(row=4, column=0, columnspan=2)

    def submit(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        marital_status = self.marital_status_entry.get()
        if name and age and gender and marital_status:
            self.__controller.insert(name, age, gender, marital_status)
            messagebox.showinfo("Success", "Employee added successfully")
            self.destroy()
