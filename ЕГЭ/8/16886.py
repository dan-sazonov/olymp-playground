import itertools

a = itertools.permutations('MATVEJ', r=6)
c = 0
for i in a:
    s = ''.join(i)
    if s.startswith('J') or s.count('AE') > 0:
        continue
    c += 1

print(c)
