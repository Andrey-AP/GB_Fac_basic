if __name__ == "__main__":
    rus_word = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
    try:
        with open('text_4.txt', 'r', encoding='UTF-8') as input_file:
            try:
                with open('out_4.txt', 'w', encoding='UTF-8') as out_file:
                    for in_line in input_file:
                        arg, val = in_line.split('-')
                        if rus_word.get(arg.strip()):
                            out_file.write(f'{rus_word.get(arg.strip())} -{val}')
                        else:
                            print(f'No {arg.strip()} in russia dict ')
            except IOError:
                print('Cannot access output file')
    except IOError:
        print('Cannot access input file')
