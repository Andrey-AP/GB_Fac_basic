class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return str(self.cell)

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell >= other.cell:
            return Cell(self.cell - other.cell)
        else:
            return "Ты дебил!"

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        if self.cell >= other.cell:
            return Cell(self.cell // other.cell)
        else:
            return "Ты опять дебил!"

    def make_order(self, row):
        cells = self.cell
        out_str = ''
        while True:
            if cells - row > 0:
                out_str = out_str + '*' * row + '\n'
                cells -= row
            else:
                out_str = out_str + '*' * cells
                break
        return out_str


c1 = Cell(8)
c2 = Cell(5)
print(c1.make_order(3))
print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 // c2)
print(c2 // c1)
