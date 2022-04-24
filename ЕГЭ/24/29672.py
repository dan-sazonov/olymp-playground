with open('2.txt') as f:
    f = f.readlines()

c = 0
for i in f:
    if i.count('E') > i.count('A'):
        c += 1

print(c)
