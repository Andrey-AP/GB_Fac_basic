class Road:
    def __init__(self, leng, wig):
        self.__length = leng
        self._width = wig

    def calc(self, ):
        return self.__length * self._width * 25 * 5


a = Road(5000, 20)

print(f'{a.calc() / 1000} т')
