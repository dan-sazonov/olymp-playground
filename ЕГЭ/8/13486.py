import itertools

a = itertools.product('ABCX', repeat=5)
c = 0

for i in a:
    if i.count('X') == 1 and (i[0] == 'X' or i[-1] == 'X'):
        c += 1

print(c)
