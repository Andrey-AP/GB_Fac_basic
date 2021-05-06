from sys import argv
try:
    path, work_hour, rate, bonus = argv
except ValueError:
    print("Not enough data")
else:
    try:
        print(f'Salary is - {float(work_hour)*float(rate)+float(bonus):.2f}')
    except ValueError:
        print('Please enter numbers')
    except Exception:
        print("Something wrong")