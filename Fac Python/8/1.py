class Data:
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    @classmethod
    def convert(cls, data_str):
        try:
            d, m, y = map(int, data_str.split('-'))
        except ValueError:
            print('Must be numbers or wrong format')
        else:
            return Data(d, m, y) if Data.check(d, m, y) else None

    @staticmethod
    def check(d, m, y):
        return True if 0 < d <= 31 and 1 <= m <= 12 and 1800 < y < 3000 else False

    def __str__(self):
        return f'Day: {self.day} Month: {self.month} Year: {self.year} '


data1 = Data.convert(input('Enter data in format dd-mm-yyyy: '))
print(data1)
