product = []
product_pattern = ['Name', 'Price', 'Amount', 'Prod unit']
int_param = ['Price', 'Amount']
prod_count = 1
while True:
    while True:
        user_choice = input(f'For add  product press 1\n'
                            f'For view analytics press 2\n'
                            f'For exit press 3\n'
                            f'>>>')
        if user_choice.isdigit() and 0 < int(user_choice) <= 3:
            user_choice = int(user_choice)
            break
        else:
            print('Please choice correct item')
            print('-' * 50)
    if user_choice == 3:
        print('Goodbye')
        break
    elif user_choice == 1:
        add_prod = {}
        for f in product_pattern:
            param = input(f'Enter param {f}: ')
            add_prod[f] = int(param) if f in int_param else param
        product.append((prod_count, add_prod))
        prod_count += 1
        print('Item added')
        print('-' * 15)

    else:

        if product:
            analys_dict = {}
            dict_struct = product[0]
            for key in dict_struct[1].keys():
                analys_dict[key] = []
            for elem in product:
                for key, val in elem[1].items():
                    analys_dict[key].append(val)
            for key, value in analys_dict.items():
                print(f'{key[:15]:>15}: {value}')
        else:
            print('Nothing to analyse')
        print('-' * 50)
