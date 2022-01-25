from math import gcd
ans = []

for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    if n == 2:
        ans.append([0, 0, 1])
        continue
    if n > 2:
        if a * c <= b * (n - 1):
            a += 1
        if a >= n - 1:
            a, b, c = 0, 0, 1
        else:
            k = gcd(a, n - 1)
            b = a // k
            c = (n - 1) // k
    ans.append([a, b, c])

for i in ans:
    print(*i)
