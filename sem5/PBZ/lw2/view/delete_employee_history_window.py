import tkinter as tk
from tkinter import messagebox

from controller.employee_history_controller import EmployeeHistoryController


class DeleteEmployeeHistoryWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.__controller: EmployeeHistoryController = EmployeeHistoryController()

        self.title("Delete Employee History")
        tk.Label(self, text="Enter Employee History ID").grid(row=0, column=0)
        self.history_id_entry = tk.Entry(self)
        self.history_id_entry.grid(row=0, column=1)

        tk.Button(self, text="Submit", command=self.submit).grid(row=1, column=0, columnspan=2)

    def submit(self):
        history_id = self.history_id_entry.get()
        if history_id:
            self.__controller.delete(history_id)
            messagebox.showinfo("Success", "Employee history deleted successfully")
            self.destroy()
