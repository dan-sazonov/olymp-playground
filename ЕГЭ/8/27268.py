import itertools

a = itertools.permutations('RUSLAN', r=6)
c = 0

for i in a:
    s = ''.join(i)
    if s.count('UA') + s.count('AU') == 0:
        c += 1

print(c)
