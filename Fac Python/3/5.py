def str_sum(p_sum, st1):
    arch_sum = p_sum
    ls = st1.split()
    for elem in ls:
        try:
            p_sum += int(elem)
        except ValueError:
            print('You must enter a number, you fucking idiot ')
            return arch_sum
    return p_sum


if __name__ == '__main__':
    my_sum = 0
    while True:
        input_str = input('Enter numbers separated by " " for exit press Q:')
        if input_str.upper() == 'Q':
            print(f'Sum was {my_sum} Goodbye!' if my_sum else 'Goodbye')
            break
        else:
            my_sum = str_sum(my_sum, input_str)
            print('Sum is - ', my_sum)
