class My_class:
    def_col = 'red'

    def __init__(self, h, w):
        self.h = h
        self.w = w


r1 = My_class(1, 5)
r2 = My_class(10, 15)

My_class.def_col = 'blue'

r1.def_col = 'green'

My_class.def_col = 'purpure'
input()