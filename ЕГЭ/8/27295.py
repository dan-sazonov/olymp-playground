import itertools

a = itertools.permutations('SVETA', r=5)
c = 0

for i in a:
    s = ''.join(i)
    if ('EA' not in s) and ('AE' not in s):
        c += 1

print(c)
