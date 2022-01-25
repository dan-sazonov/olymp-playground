n, m = map(int, input().split())
arr = list(map(int, input().split()))
p = [0] * (n + 1)

for i in range(1, n + 1):
    p[i] = p[i - 1] + arr[i - 1]

for _ in range(m):
    lj, rj = map(int, input().split())
    print(p[rj] - p[lj - 1])
