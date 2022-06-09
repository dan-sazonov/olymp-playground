import itertools

a = itertools.product('NASTY', repeat=6)
c = 0

for i in a:
    if i.count('A') <= 1 and i.count('Y') <= 1:
        c += 1

print(c)
