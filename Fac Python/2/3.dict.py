season_dict = {'1': 'Winter', '2': 'Winter', '3': 'Spring', '4': 'Spring', '5': 'Spring', '6': 'Summer',
               '7': 'Summer', '8': 'Summer', '9': 'Autumn', '10': 'Autumn', '11': 'Autumn', '12': 'Winter'}

while True:
    mon = input('Enter month number:')
    if mon.isdigit() and 0 < int(mon) <= 12:
        print(season_dict[mon])
        break
    else:
        print('You need enter a number between 0 and 12')
