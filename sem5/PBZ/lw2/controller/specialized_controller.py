from model.specialized_repo import SpecializedRepository


class SpecializedController:
    def __init__(self) -> None:
        self.__repo: SpecializedRepository = SpecializedRepository()

    def staffing_schedule(self, department_id: str) -> list[tuple]:
        return self.__repo.staffing_schedule(department_id)

    def female_employee_list(self) -> list[tuple]:
        return self.__repo.female_employee_list()

    def special_employee_list(self, position_id: str, age_boarder: str) -> list[tuple]:
        return self.__repo.special_employee_list(position_id, age_boarder)
