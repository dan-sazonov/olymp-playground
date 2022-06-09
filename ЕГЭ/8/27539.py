import itertools

a = set(itertools.product('BORIS', repeat=6))
c = 0

for i in a:
    if i.count('R') == 1 and i.count('B') == 1 and i.count('S') <= 1:
        c += 1

print(c)
