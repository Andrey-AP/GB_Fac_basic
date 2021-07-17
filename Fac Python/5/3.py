if __name__ == "__main__":
    with open("text_3.txt", "r", encoding="UTF-8") as sal_doc:
        # sal_doc_lines = sal_doc.readlines()
        sal_a = 0
        emp_counter = 0
        for line in sal_doc:
            surname, sal = line.split(' ')
            try:
                sal_a += float(sal)
                emp_counter += 1
                if float(sal) < 20000:
                    print(surname)
            except ValueError:
                print(f"-->Invalid salary format for employ {surname}<--")
        print(f"Average salary is: {sal_a/emp_counter}")


