n = int(input())
a = list(map(int, input().split()))
p = [0] * (n + 1)
i_best = j_best = i_min = 0

for i in range(1, n + 1):
    p[i] = p[i - 1] + a[i - 1]

for j in range(1, n):
    if p[j] < p[i_min] and p[j] % 3 == 0:
        i_min = j
    if p[j + 1] - p[i_min] > p[j_best] - p[i_best] and (p[j + 1] - p[i_min]) % 3 == 0:
        j_best = j
        i_best = i_min

print(i_best + 1, j_best + 1)
