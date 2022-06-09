import itertools

a = itertools.product('ANDREJ', repeat=4)
c = 0

for i in a:
    if i[0] != 'J' and (i.count('A') >= 1 or i.count('E') >= 1):
        c += 1

print(c)
