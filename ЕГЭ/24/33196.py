with open('4.txt') as f:
    f = f.read()

c = dict()
for i in range(len(f)-1):
    if f[i] == 'A':
        if f[i+1] in c.keys():
            c[f[i+1]] += 1
        else:
            c[f[i + 1]] = 1

print(sorted(c.items(), key=lambda x: x[1], reverse=True))
