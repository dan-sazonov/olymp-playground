n = int(input())
tm = sorted([(int(input()), c) for c in range(n)])
i = 0
j = 1
total = sum(tm[c][0] for c in range(i, j + 1))
res = total
# print(tm, tm[j + 1][0])
n = len(tm)
while not(j > n) or not(i > n):
    try:
        if tm[j][0] < tm[i][0] + tm[i+1][0]:
            j += 1
            if total > res:
                res = total
        else:
            i += 1
    except IndexError:
        print(j, [i], tm, len(tm))
    total = sum(tm[c][0] for c in range(i, (j + 1) if (j + 1) < n else j))
    print(i, j)
print(tm, total)

