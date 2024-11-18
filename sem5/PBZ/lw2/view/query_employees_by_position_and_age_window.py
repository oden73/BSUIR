import tkinter as tk
from tkinter import ttk

from controller.specialized_controller import SpecializedController


class QueryEmployeesByPositionAndAgeWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.__controller: SpecializedController = SpecializedController()

        self.title("Query Employees By Position And Age")
        tk.Label(self, text="Enter Position ID").grid(row=0, column=0)
        self.position_id_entry = tk.Entry(self)
        self.position_id_entry.grid(row=0, column=1)

        tk.Label(self, text="Enter Maximum Age").grid(row=1, column=0)
        self.max_age_entry = tk.Entry(self)
        self.max_age_entry.grid(row=1, column=1)

        tk.Button(self, text="Submit", command=self.submit).grid(row=2, column=0, columnspan=2)

    def submit(self):
        position_id = self.position_id_entry.get()
        max_age = self.max_age_entry.get()
        if position_id and max_age:
            result_window = tk.Toplevel(self)
            result_tree = ttk.Treeview(result_window)
            result_tree['columns'] = ('Name', 'Age', 'Department Name', 'Position Name')
            result_tree.column("#0", width=0, stretch=tk.NO)
            for column in result_tree['columns']:
                result_tree.column(column, anchor=tk.W, width=100)
                result_tree.heading(column, text=column, anchor=tk.W)

            rows = self.__controller.special_employee_list(position_id, max_age)

            for row in rows:
                result_tree.insert('', 'end', values=row)
            result_tree.pack(fill=tk.BOTH, expand=True)

            def close_window():
                if result_window.winfo_exists():
                    result_window.destroy()

            result_window.after(10000, close_window)
