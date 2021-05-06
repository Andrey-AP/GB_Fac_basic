my_list = [3, 5.85, 'strd', True, [5, 7], {'f': 5, 7: 'dd'}, ('v', 7), (5 - 8j), b'twelve', range(5),
           zip(*['1', '2', ' 3'], ['1', ' 2', '3'])]
type_list = []
for elem in my_list:
    type_list.append((type(elem)))
for ind, elem in enumerate(type_list, 1):
    print(f'{ind}.{my_list[ind - 1]} --> {elem}')
