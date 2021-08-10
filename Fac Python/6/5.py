class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title} класс Stationary')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} класс Pen ')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} класс Pencil ')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} класс Handle ')


if __name__ == '__main__':
    st1 = Stationery('1')
    pen1 = Pen('pen')
    penc1 = Pencil('pencil')
    ha = Handle('handle')
    st1.draw()
    pen1.draw()
    penc1.draw()
    ha.draw()
