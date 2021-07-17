if __name__ == "__main__":
    try:
        with open("1_pr.txt", 'w', encoding='UTF-8') as woo:
            while True:
                in_str = input("Enter a string for adding in file: ")
                if in_str:
                    woo.write(f'{in_str}\n')
                else:
                    break
    except EOFError:
        print("Some fucking error")

    try:
        with open("1_pr.txt", 'r', encoding='UTF-8') as woo:
            lines = woo.readlines()
            line = 1
            for item in lines:
                words = item.split(' ')
                word_count = 0
                for word in words:
                    if word and word != '\n':
                        word_count += 1
                print(f"line number:{line} contain {word_count} words")
                line += 1
    except EOFError:
        print("Some fucking error")
