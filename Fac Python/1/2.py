sec = int(input('Введите секунды: '))
print(f'{sec//3600:02}:{sec%3600//60:02}:{sec%3600%60:02}')