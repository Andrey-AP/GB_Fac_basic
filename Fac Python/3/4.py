def my_pow1(a, b):
    return a ** b


def my_pow2(a, b):
    a1 = a
    for i in range(1,abs(b)):
        a *= a1
    return 1 / a


if __name__ == "__main__":
    print(my_pow1(int(input('Enter a:')), int(input('Enter b:'))))
    print(my_pow2(int(input('Enter a:')), int(input('Enter b:'))))
