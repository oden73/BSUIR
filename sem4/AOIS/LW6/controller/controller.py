from output.printer import Printer
from output.inputer import Inputer
from hash.hash_table import HashTable


class Controller:
    def __init__(self):
        self.printer: Printer = Printer()
        self.inputer: Inputer = Inputer()

        self.hash_table: HashTable = HashTable()

    def run(self):
        while True:
            print(self.hash_table.hash_table)
            self.printer.print_operation_header()
            operation_char: str = self.inputer.enter_operation_char()
            match operation_char:
                case '1':
                    print(self.hash_table)
                    self.printer.print_hash_table(self.hash_table.get_print_view())
                case '2':
                    self.printer.print_add_element()
                    ID, Pi = self.inputer.enter_add_element()
                    self.hash_table.add_element(ID, Pi)
                    self.printer.print_operation_complete()
                case '3':
                    self.printer.print_search_element()
                    ID: str = self.inputer.enter_ID()
                    Pi: str = self.hash_table.find_by_id(ID)
                    self.printer.print_search_result(Pi)
                case '4':
                    try:
                        self.printer.print_update_element()
                        ID: str = self.inputer.enter_ID()
                        Pi: str = self.inputer.enter_Pi()
                        self.hash_table.update_by_id(ID, Pi)
                        self.printer.print_operation_complete()
                    except ValueError as _:
                        self.printer.print_element_not_found()
                case '5':
                    try:
                        self.printer.print_delete_element()
                        ID: str = self.inputer.enter_ID()
                        self.hash_table.delete_by_id(ID)
                        self.printer.print_operation_complete()
                    except ValueError as _:
                        self.printer.print_element_not_found()
                case '0':
                    exit(0)
                case _:
                    self.printer.print_unknown_operation()
