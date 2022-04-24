with open('10.txt') as f:
    f = f.readlines()

s = ''
c = 1_000_001

for i in f:
    if i.count('N') < c:
        s = i
        c = i.count('N')
t = dict()
for i in s:
    if i in t.keys():
        t[i] += 1
    else:
        t[i] = 1

print(sorted(t.items(), key=lambda x: x[1], reverse=True))
