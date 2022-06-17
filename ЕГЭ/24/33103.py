c = 0

for i in open('33103.txt').readlines():
    if i.count('A') > i.count('E'):
        c += 1

print(c)
