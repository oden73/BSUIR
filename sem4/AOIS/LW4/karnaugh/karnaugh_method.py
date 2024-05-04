class Karnaugh:
    def form_table(self) -> list[list[str]]:
        pass

    def form_final_normal_form_fields(self) -> list[list[tuple]]:
        pass

    def form_field(self, initial_index: tuple, value: str) -> list[tuple]:
        pass

    def possibility_to_go_top(self, indexes: list[tuple], value: str) -> list[tuple]:
        pass

    def possibility_to_go_down(self, indexes: list[tuple], value: str) -> list[tuple]:
        pass

    def form_final_normal_form_arguments(self) -> list[list[str]]:
        pass

    def final_normal_form(self) -> str:
        pass

    def print_table(self) -> None:
        pass
