import tkinter as tk
from tkinter import ttk


class AddEmployeeWindow(tk.Tk):
    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.title("Добавление сотрудника")

        # Создание форм ввода
        tk.Label(self, text="Full Name").grid(row=0, column=0)
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1)

        tk.Label(self, text="Age").grid(row=1, column=0)
        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=1, column=1)

        tk.Label(self, text="Gender").grid(row=2, column=0)
        self.entry_gender = tk.Entry(self)
        self.entry_gender.grid(row=2, column=1)

        tk.Label(self, text="Marital Status").grid(row=3, column=0)
        self.entry_marital_status = tk.Entry(self)
        self.entry_marital_status.grid(row=3, column=1)

        # Кнопка добавления сотрудника
        btn_add = tk.Button(self, text="Add", command=self.add_employee)
        btn_add.grid(row=4, columnspan=2)

    def add_employee(self) -> None:
        pass
