proceeds = int(input('Enter proceeds:'))
loss = int(input('Enter loss:'))

if proceeds < loss:
    print('Bad news, your firm is sucks')
elif proceeds == loss:
    print('Not so bad, try in next month')
else:
    print('Good news, you have profit')
    print(f'Profitability is: {proceeds / loss:.2f}')
    staff = int(input('Enter number of staff:'))
    print(f"Profit per employee: {(proceeds - loss) / staff:.2f}")
