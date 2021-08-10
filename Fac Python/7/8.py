class Myclass:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    @classmethod
    def set_fio(cls, data):
        nam, sur = data
        return cls(nam, sur)

    @staticmethod
    def get_fio(obj):
        obj.n = 'gggg'
        return f'{obj.n} {obj.s}'


my_list = ['nah', 'hui']

my_1 = Myclass.set_fio(my_list)
print(my_1.get_fio(my_1))
print(my_1.n)
