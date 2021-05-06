from functools import reduce


def my_mult(a, b):
    return a * b


ls = [elem for elem in range(100, 1001) if elem % 2 == 0]
print(reduce(my_mult, ls))
