ls1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 10, 123, 55, 185]
print(' '.join(map(str, (ls1[ind] for ind in range(1, len(ls1)) if ls1[ind] > ls1[ind - 1]))))
