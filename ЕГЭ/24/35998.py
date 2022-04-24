with open('1.txt') as f:
    f = f.readlines()
m = 0
for i in f:
    if i.count('A') >= 25:
        continue
    i = i.rstrip('\n')
    tmp = 0
    for j in range(len(i)):
        tmp = max(tmp, i.rfind(i[j]) - j)
    m = max(m, tmp)

print(m)
