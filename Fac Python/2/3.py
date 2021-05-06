winter = ['1', '2', '12']
spring = ['3', '4', '5']
summer = ['6', '7', '8']


while True:
    mon = input('Enter month number:')
    if mon.isdigit() and 0 < int(mon) <= 12:
        break
    else:
        print('You need enter a number betvi 0 and 12')
if mon in winter:
    print('Winter')
elif mon in spring:
    print('Spring')
elif mon in summer:
    print('Summer')
else:
    print('Autumn')
