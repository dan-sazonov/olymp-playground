with open('9.txt') as f:
    f = f.read()

c = 0
m = 0
for i in range(len(f)):
    c += 1
    if f[i] == 'K' and f[i+1] == 'L' or f[i] == 'L' and f[i+1] == 'K':
        m = max(c, m)
        c = 0

print(m)
