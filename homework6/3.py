class Worker:
    name: str
    surname: str
    position: str

    _income = {"wage": 0, "bonus": 0}

    def __init__(self, worker_name: str, worker_surname: str, worker_position: str, worker_wage: int, worker_bonus: int):
        self.name = worker_name
        self.surname = worker_surname
        self.position = worker_position
        self._income["wage"] = worker_wage
        self._income["bonus"] = worker_bonus


class Position(Worker):
    def get_full_name(self):
        print(f"Full name of the worker is {self.name} {self.surname}.")

    def get_total_income(self):
        print(f"Total income of the worker is {self._income['wage'] + self._income['bonus']}.")


first_worker = Position("Brian", "O'Conner", "CEO", 3000, 1500)
first_worker.get_full_name()
first_worker.get_total_income()
