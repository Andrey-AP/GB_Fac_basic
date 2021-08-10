class MyZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_dev(a, b):
    try:
        if b == 0:
            raise MyZeroDiv('Delenie na 0? you are debil')
        else:
            return a / b
    except MyZeroDiv as err:
        print(err)


c = my_dev(3, 2)
print(c)
