n, d = map(int, input().split())
a = list(map(int, input().split()))
used = set()
ans = 0

for i in enumerate(a):
    best = set()
    if i in used:
        continue
    for j in enumerate(a):
        # print(i,j, j==i)
        if j == i or j in used:
            # print('err', i, j)
            continue
        elif i[1] + j[1] <= d:
            best.add(j)
    if not best:
        used.add(i)
        ans += 1
    else:
        ans += 1
        t = max(best, key=lambda x: x[1])
        used = used.union({i, j})
        # print(i, '=', best, t)

print(ans - 1)
