from math import modf as mo


def gen_input():
    while True:
        try:
            begin = int(input('Enter begin of range:'))
            end_range = int(input('Enter end of range:'))
            if begin < end_range:
                ret_str = ' '.join(str(elem) for elem in range(begin, end_range + 1))
                break
            else:
                print('End of range must be grate than begin of range')
        except ValueError:
            print('Mus be an integer number')
    return ret_str


def man_input():
    ret_str = ''
    while True:
        elem = input('Enter a number for adding, for End press Q:')
        if elem != 'q' and elem != 'Q':
            if elem.isdigit():
                ret_str = ret_str + elem + ' '
            else:
                print('You must enter a number')
        else:
            break
    return ret_str


def mk_ch():
    while True:
        print(f'howe would you like to create a input file\n' +
              '1 using generator\n' +
              '2. manual entry\n' +
              'For exit press 3')
        select_res = input('--->')
        try:
            select_res = int(select_res)
            if select_res == 3:
                input('Good by!')
                exit()
            elif 0 < select_res < 3:
                return select_res
            else:
                print('no such variant')
        except ValueError:
            print('You are idiot')


def write_to_file(input_str, file_name):
    if input_str:
        try:
            with open('file_name', 'a', encoding='UTF-8') as out_file:
                out_file.write(input_str + '\n')
        except IOError:
            print('Cannot access output file')


def get_line(file_name):
    try:
        with open(file_name, 'r', encoding='UTF-8') as in_file:
            for line in in_file:
                yield line
    except IOError:
        print('Cannot access output file')


def aver2(file_name):
    line_count = 0
    for line in get_line(file_name):
        line = line.strip('\n')
        summ = 0.0
        line_count += 1
        list_for_count = line.split(' ')
        for elem in list_for_count:
            try:
                summ += float(elem)
            except ValueError:
                pass
        wh = mo(summ)
        if wh[0] != 0.0:
            print(f'Sum of elements in {line_count} is - {summ}')
        else:
            print(f'Sum of elements in {line_count} is - {int(wh[1])}')


def aver(file_name):
    line_count = 0
    try:
        with open(file_name, 'r', encoding='UTF-8') as in_file:
            for line in in_file:
                line = line.strip('\n')
                summ = 0.0
                line_count += 1
                list_for_count = line.split(' ')
                for elem in list_for_count:
                    try:
                        summ += float(elem)
                    except ValueError:
                        pass
                wh, fr = str(summ).split('.')
                if fr == '0':
                    print(f'Sum of elements in {line_count} is - {wh}')
                else:
                    print(f'Sum of elements in {line_count} is - {summ}')
    except IOError:
        print('Cannot access output file')


if __name__ == '__main__':
    file_name = 'text_5.txt'
    select = mk_ch()
    if select == 1:
        in_str = gen_input()
    else:
        in_str = man_input()
    write_to_file(in_str, file_name)
    aver(file_name)
    aver2(file_name)
