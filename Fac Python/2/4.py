my_list = input("Enter elements separated by space: ").split()
for ind, elem in enumerate(my_list, 1):
    print(f'{ind}. {elem}' if len(elem) <= 10 else f'{ind}. {elem[:10]}')
