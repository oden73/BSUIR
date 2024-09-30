import tkinter as tk
from tkinter import ttk

from view.add_employee_window import AddEmployeeWindow


# двойное нажатие на сотрудника - открытие таблицы с его историей перевода


class MainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Государственное предприятие')

        # widgest creation

        # table
        self.tree = ttk.Treeview(self, columns=("ID", "Full Name", "Age", "Gender", "Marital Status"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Full Name", text="Full Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Marital Status", text="Marital Status")
        self.tree.pack(padx=10, pady=10)

        # Создание фрейма для кнопок
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        # Кнопка для открытия окна добавления сотрудника
        self.btn_add_employee = tk.Button(button_frame, text="Добавить сотрудника", command=self.open_add_employee_window)
        self.btn_add_employee.grid(row=0, column=0, padx=5)

        # Кнопка для осуществления перевода
        self.btn_transfer_employee = tk.Button(button_frame, text="Осуществление перевода",
                                               command=self.open_transfer_window)
        self.btn_transfer_employee.grid(row=0, column=1, padx=5)

        # Кнопка для запроса 1
        self.btn_query1 = tk.Button(button_frame, text="Запрос 1", command=self.execute_query1)
        self.btn_query1.grid(row=0, column=2, padx=5)

        # Кнопка для запроса 2
        self.btn_query2 = tk.Button(button_frame, text="Запрос 2", command=self.execute_query2)
        self.btn_query2.grid(row=0, column=3, padx=5)

        # Кнопка для запроса 3
        self.btn_query2 = tk.Button(button_frame, text="Запрос 3", command=self.execute_query3)
        self.btn_query2.grid(row=0, column=4, padx=5)

    def open_add_employee_window(self) -> None:
        AddEmployeeWindow(self)

    def open_transfer_window(self) -> None:
        pass

    def execute_query1(self):
        pass

    def execute_query2(self):
        pass

    def execute_query3(self):
        pass


c = MainWindow()
c.mainloop()
