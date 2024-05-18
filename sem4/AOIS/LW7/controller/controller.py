from input_ouput.printer import Printer
from input_ouput.inputer import Inputer
from table.binary_table import BinaryTable


class Controller:
    def __init__(self):
        self.printer: Printer = Printer()
        self.inputer: Inputer = Inputer()
        self.table: BinaryTable = BinaryTable()

    def run(self) -> None:
        while True:
            self.printer.print_operations()
            operation_key: str = self.inputer.enter_operation_key()
            match operation_key:
                case '1':
                    self.printer.print_table(self.table.table)
                case '2':
                    self.printer.print_get_word_by_index()
                    index: int = self.inputer.enter_index()
                    word: str = self.table.get_word_str(self.table.get_word_by_index(index))
                    self.printer.print_word_by_index(word)
                case '3':
                    self.printer.print_update_word_by_index()
                    index: int = self.inputer.enter_index()
                    new_word: str = self.inputer.enter_string()
                    self.table.update_word_by_index(new_word, index)
                    self.printer.operation_complete()
                case '4':
                    self.printer.print_get_address_column_by_index()
                    index: int = self.inputer.enter_index()
                    address_column: str = self.table.get_word_str(self.table.get_address_column_by_index(index))
                    self.printer.print_address_column_by_index(address_column)
                case '5':
                    self.printer.print_update_address_column_by_index()
                    index: int = self.inputer.enter_index()
                    new_address_column: str = self.inputer.enter_string()
                    self.table.update_address_column_by_index(new_address_column, index)
                    self.printer.operation_complete()
                case '6':
                    self.printer.print_logical_functions()
                    index1, index2, index3 = (self.inputer.enter_index(), self.inputer.enter_index(),
                                              self.inputer.enter_index())
                    function: str = self.inputer.enter_string()
                    self.table.logical_operation(index1, index2, index3, function)
                    self.printer.operation_complete()
                case '7':
                    self.table.sort()
                    self.printer.operation_complete()
                case '8':
                    self.printer.print_string_key()
                    key: str = self.inputer.enter_string()
                    self.table.word_sum(key)
                    self.printer.operation_complete()
                case '0':
                    exit(0)
                case _:
                    self.printer.unknown_operation()
