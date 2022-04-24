with open('13.txt') as f:
    f = f.read()

m = 0
c = 0
for i in range(len(f) - 3):
    c += 1
    if f[i] == 'X' and f[i + 1] == f[i + 2] == 'Z' and f[i + 3] == 'Y':
        m = max(c + 2, m)
        c = 0
else:
    if c != 0:
        m = max(c + 3, m)

print(m)
