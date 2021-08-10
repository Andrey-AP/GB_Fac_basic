from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, v, h):
        self.v = v
        self.h = h
        c = v // h

    @property
    @abstractmethod
    def calcul(self):
        pass


class Coat(Clothes):
    @property
    def calcul(self):
        return round(self.v / 6.5 + 0.5, 3)


class Suit(Clothes):
    @property
    def calcul(self):
        return round(self.h * 2 + 0.3, 3)


c = Coat(2, 5)
s = Suit(8, 9)
print(c.calcul)
print(s.calcul)
