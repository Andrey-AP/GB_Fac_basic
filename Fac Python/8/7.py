class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a
        return Complex(a, b)

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a, b)

    def __str__(self):
        return f'{self.a}{self.b}i'


com1 = Complex(3, 1)
comp2 = Complex(2, -3)

print(com1 * comp2)

print(com1+comp2)
