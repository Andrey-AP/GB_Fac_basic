rate_list = []
while True:
    while True:
        ch = input(f'For add element in rating press - 1 \n'
                   'For see ratin press - 2\n'
                   'For exit press - 3 \n'
                   '>>>')
        if ch.isdigit() and 0 < int(ch) <= 3:
            ch = int(ch)
            break
        else:
            print("wrong choice")
    if ch == 3:
        print('Goodbye')
        break
    elif ch == 1:
        elem = input('enter element:')
        if elem.isdigit():
            elem = int(elem)
            if not rate_list:
                rate_list.append(elem)
            elif elem in rate_list:
                rate_list.insert(rate_list.index(elem), float(elem))
            else:
                if elem > rate_list[-1]:
                    rate_list.append(elem)
                elif elem < rate_list[0]:
                    rate_list.insert(0, elem)
                else:
                    for ind in range(1, len(rate_list) - 1):
                        if rate_list[ind] > elem:
                            rate_list.insert(ind, elem)
        else:
            print(f'You must enter a natural number\n')
    else:
        print('Rate list:', *rate_list[::-1])
        # print(f'Rate list:', end='')
        # for elem in rate_list[::-1]:
        #     print(elem, end=' ')
        # print()
