s = []

for i in input():
    if i not in s:
        s.append(i)

print(*s, sep='')
