import itertools

a = tuple(itertools.permutations(range(0,8), r=5))
c = 0

for i in a:
    flag = 1
    for j in range(4):
        if ((i[j] % 2) + (i[j+1] % 2)) != 1:
            flag = 0
    c += flag

print(c)
