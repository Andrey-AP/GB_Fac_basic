a = int(input('Enter value a: '))
b = int(input('Enter value b: '))
day_count = 1
while True:
    if a >= b:
        print(f'On {day_count} day sportsman reached the goal')
        break
    else:
        a += a * 0.1
        day_count += 1
