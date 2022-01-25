groups = []
pots = [input() for _ in range(int(input()))]

for _ in range(int(input())):
    tmp = []
    for _ in range(int(input())):
        tmp.append(int(input()))
    groups.append(tmp)

for i in groups:
    new = []
    for j in i:
        new.append(pots[j - 1])
    pots = new.copy()

print(*pots, sep='\n')
