n, t = map(int, input().split())
ans = 0
pigs = list(map(int, input().split()))
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

for i in range(1, n + 1):
    pigs[i - 1] = i, pigs[i - 1]
    distances[i - 1] = i, prices[i - 1] - distances[i - 1] * t

pigs.sort(key=lambda x: x[1])
distances.sort(key=lambda x: x[1])

res = [[distances[i - 1][0], pigs[i - 1][0]] for i in range(1, n + 1)]
for _, j in sorted(res, key=lambda x: x[0]):
    print(j, end=' ')
