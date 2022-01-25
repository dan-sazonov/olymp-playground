n = int(input())
p = [0] * (n + 1)
a = [int(input()) for _ in range(n)]
i_best = j_best = i_min = 0
ans = []

for i in range(1, n + 1):
    p[i] = p[i - 1] + a[i - 1]

for j in range(1, n):
    if p[j] < p[i_min]:
        i_min = j
    if p[j + 1] - p[i_min] > p[j_best] - p[i_best]:
        ans.append([i_best, j_best])
        j_best = j
        i_best = i_min
ans.append([i_best, j_best])
print(ans)
