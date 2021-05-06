def my_fact(a):
    res = 1
    for i in range(1, a + 1):
        res *= i
        yield res


n = 5
for elem in my_fact(n):
    print(elem)
