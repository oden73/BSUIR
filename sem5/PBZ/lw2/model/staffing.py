class Staffing:
    def __init__(self, id: int, department_id: int, position_id: int, quantity: int) -> None:
        self.id: int = id
        self.department_id: int = department_id
        self.position_id: int = position_id
        self.quantity: int = quantity
