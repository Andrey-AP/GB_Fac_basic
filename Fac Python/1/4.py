n = int(input('Enter a number: '))
my_max = n % 10
while n:
    if n % 10 > my_max:
        my_max = n % 10
    if my_max == 9:
        break
    n //= 10
print(my_max)
