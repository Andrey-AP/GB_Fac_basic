def get_line(fname):
    try:
        with open(fname, 'r', encoding='UTF-8') as in_file:
            for line in in_file:
                yield line
    except IOError:
        print('Cannot access file!')


if __name__ == '__main__':
    file_name = 'text_6.txt'
    out_dict = {}
    for line in get_line(file_name):
        subj, *clock = line.split(' ')
        subj_time = 0
        for item in clock:
            if item != '-':
                try:
                    item = int(item[:item.find('(')])
                    subj_time += item
                except ValueError:
                    print('Не верный формат времени!')
        out_dict[subj] = subj_time
    print(out_dict)
