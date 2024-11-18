import tkinter as tk
from tkinter import ttk

from controller.specialized_controller import SpecializedController


class QueryStaffingWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.__controller: SpecializedController = SpecializedController()

        self.title("Query Staffing")
        tk.Label(self, text="Enter Department ID").grid(row=0, column=0)
        self.department_id_entry = tk.Entry(self)
        self.department_id_entry.grid(row=0, column=1)

        tk.Button(self, text="Submit", command=self.submit).grid(row=1, column=0, columnspan=2)

    def submit(self):
        department_id = self.department_id_entry.get()
        if department_id:
            result_window = tk.Toplevel(self)
            result_tree = ttk.Treeview(result_window)
            result_tree['columns'] = ('Position Name', 'Short Name', 'Code', 'Lower Tariff Rank', 'Upper Tariff Rank', 'Quantity')
            result_tree.column("#0", width=0, stretch=tk.NO)
            for column in result_tree['columns']:
                result_tree.column(column, anchor=tk.W, width=100)
                result_tree.heading(column, text=column, anchor=tk.W)

            rows = self.__controller.staffing_schedule(department_id)

            for row in rows:
                result_tree.insert('', 'end', values=row)
            result_tree.pack(fill=tk.BOTH, expand=True)

            def close_window():
                if result_window.winfo_exists():
                    result_window.destroy()

            result_window.after(10000, close_window)

