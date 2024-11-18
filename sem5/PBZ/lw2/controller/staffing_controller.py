from model.staffing_repo import StaffingRepository
from model.staffing import Staffing


class StaffingController:
    def __init__(self) -> None:
        self.__repo: StaffingRepository = StaffingRepository()

    def select(self) -> list[tuple]:
        staffing_list: list[Staffing] = self.__repo.select()

        result_list: list[tuple] = []
        for staffing in staffing_list:
            result_list.append((str(staffing.id), str(staffing.department_id), str(staffing.position_id),
                                str(staffing.quantity)))

        return result_list
