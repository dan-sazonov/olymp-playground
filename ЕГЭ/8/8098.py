import itertools

a = itertools.product('CLON', repeat=5)
x = 0

for i in a:
    if i.count('C') == 1:
        x += 1

print(x)
