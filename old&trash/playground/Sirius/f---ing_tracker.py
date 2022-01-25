amount = 115
current = 0

while current <= amount:
    input('Нажми Enter, если решил задачу')
    current += 1
    print('Молодца, осталось', amount - current)
    print('Сейчас решено ~{0}%'.format(int(current/amount * 100)))
    print('=====')
print('Все, закончились')
input()
