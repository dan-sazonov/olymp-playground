import itertools

a = itertools.product('ANDREJ', repeat=7)
c = 0

for i in a:
    if (i.count('A') + i.count('J') == 2) and i[0] != 'J':
        c += 1

print(c)
