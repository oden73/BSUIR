from hash.cell import Cell


class HashTable:
    def __init__(self):
        self.capacity: int = 2
        self.hash_table: dict = {}
        self.cells_list: list[Cell] = []

    def add_element(self, ID: str, Pi: str):
        self.capacity += 1
        self.rehash()

        new_cell: Cell = Cell(ID, Pi, self.capacity)
        self._add_cell(new_cell)
        self.cells_list.append(new_cell)

    def _add_cell(self, new_cell: Cell):
        if new_cell.h not in self.hash_table:
            self.hash_table[new_cell.h] = new_cell

        else:
            last_cell_in_chain: Cell = self.hash_table[new_cell.h]
            while last_cell_in_chain.next:
                last_cell_in_chain = last_cell_in_chain.next
            last_cell_in_chain.next = new_cell

    def find_by_id(self, ID: str) -> str:
        cell: Cell = Cell(ID=ID, capacity=self.capacity)

        if cell.h not in self.hash_table:
            return 'Nothing was found'

        else:
            cell = self.hash_table[cell.h]
            while cell.ID != ID and cell:
                cell = cell.next
            return cell.Pi

    def delete_by_id(self, ID: str) -> None:
        cell: Cell = Cell(ID=ID, capacity=self.capacity)

        if cell.h not in self.hash_table:
            raise ValueError

        else:
            cell = self.hash_table[cell.h]

            while cell.ID != ID and cell:
                cell = cell.next

            if not cell:
                raise ValueError

            if cell.ID == self.hash_table[cell.h].ID:
                self.hash_table[cell.h] = cell.next
            else:
                cell.prev = cell.next

            for cell in self.cells_list:
                if cell.ID == ID:
                    self.cells_list.remove(cell)

            self.capacity -= 1
            self.rehash()

    def update_by_id(self, ID: str, new_Pi: str) -> None:
        cell: Cell = Cell(ID=ID, capacity=self.capacity)

        if cell.h not in self.hash_table:
            raise ValueError

        else:
            cell = self.hash_table[cell.h]
            while cell.ID != ID and cell:
                cell = cell.next
            cell.Pi = new_Pi

    def rehash(self):
        self.hash_table = {}

        for cell in self.cells_list:
            cell.generate_h(self.capacity)
            cell.prev = None
            cell.next = None
            self._add_cell(cell)

    def get_print_view(self) -> list[tuple]:
        # ID V h U in-hash-pos Pi
        print_view: list[tuple] = []
        for h in sorted(self.hash_table.keys()):
            nested_position = 0
            cell = self.hash_table[h]
            while cell:
                print_view.append((cell.ID, str(cell.V), str(cell.h), str(cell.U), f'{h}.{nested_position}', cell.Pi))
                nested_position += 1
                cell = cell.next
        return print_view
