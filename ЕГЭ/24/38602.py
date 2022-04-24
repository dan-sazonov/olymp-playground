with open('7.txt') as f:
    f = f.read()

m = 0
c = 0
for i in range(len(f)):
    c += 1
    if f[i] == 'P' and f[i+1] == 'P':
        m = max(c, m)
        c = 0

print(m)
