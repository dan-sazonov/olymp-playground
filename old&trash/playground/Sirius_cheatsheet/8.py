N, T = map(int, input().split())
red = 0
pigs = list(map(int, input().split()))
cities = list(map(int, input().split()))
cent = list(map(int, input().split()))
for i in range(1, N + 1):
    pigs[i - 1] = (i, pigs[i - 1])
    cities[i - 1] = (i, cent[i - 1] - cities[i - 1] * T)
pigs.sort(key=lambda x: x[1])
cities.sort(key=lambda x: x[1])
res = []
for i in range(1, N + 1):
    res.append((cities[i - 1][0], pigs[i - 1][0]))
res.sort(key=lambda x: x[0])
print(" ".join([str(x[1]) for x in res]))
