n = int(input())
k = c = 0
res = []
for o, p, q in zip(range(1, n + 1), tuple(map(int, input().split())), tuple(map(int, input().split()))):
    res.append([o, p, q, p + q])
res.sort(key=lambda x: x[3], reverse=True)

for i in range(n - 1, -1, -1):
    tmp = res[i][2] - c
    c += res[i][1]
    if tmp <= 0:
        res = [[-1, 0]]
        break

for j in res:
    print(j[0], end=' ')
