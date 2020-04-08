class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name, self.surname, self.position, self.wage, self.bonus = name, surname, position, wage, bonus
        list_incam = {"wage": wage, "bonus": bonus}
        self._incam = list_incam["wage"]
    def print(self):
        print(self.income)

class Position(Worker):
    def get_full_name(self):
        print(f"{name} {surname}")
    def get_total_income(self):
        print(f"{self.bonus + self.wage}")
