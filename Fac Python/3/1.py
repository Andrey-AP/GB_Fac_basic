def my_funct(a, b):
    try:
        return round(a / b, 4)
    except ZeroDivisionError:
        print('Error - zero division')


print(my_funct(float(input('enter a: ')), float(input('Enter b:'))))
