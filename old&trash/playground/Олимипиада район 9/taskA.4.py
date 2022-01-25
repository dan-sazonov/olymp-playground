foo = open('input.in').read().split('\n') #читаем ввесь файл, получаем список, где каждый элемент = содерж строки
amount = int(foo[0])
for c in range(1, amount + 1):
    x = foo.count(foo[c])
    if x == 1:
        print(foo[c])
        break
