def max_summ(a, b, c):
    num_list = [a, b, c]
    max1 = max(num_list)
    num_list.remove(max1)
    max2 = max(num_list)
    return max1 + max2


if __name__ == "__main__":
    print(max_summ(10, 2, 1))
