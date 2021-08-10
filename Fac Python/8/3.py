class MyExcept(Exception):
    def __init__(self, txt):
        self.txt = txt


ls = []
while True:
    in_num = input('Enter a number, for exit press Enter:')
    if in_num == '':
        break
    else:
        try:
            if in_num.replace('-', '').replace('.', '').isdigit():
                ls.append(float(in_num))
            else:
                raise MyExcept('not a number')
        except MyExcept as err:
            print(err)
print(ls)
