class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return [self.name, self.surname, sum(self._income.values())]


w1 = Position('last', 'hu', 'wor', 5000.20, 100)
print(*w1.get_full_name())