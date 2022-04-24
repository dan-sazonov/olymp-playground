with open('3.txt') as f:
    i = f.read()
c = dict()

for j in range(len(i)-2):
    if i[j] == i[j+2]:
        if i[j+1] not in c.keys():
            c[i[j+1]] = 1
        else:
            c[i[j + 1]] += 1

print(sorted(c.items(), key=lambda x: x[1], reverse=True))
