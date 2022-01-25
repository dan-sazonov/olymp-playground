n = int(input())

r = 1
ans = 0
while r * r <= n:
    ans += 1
    n -= r * r
    r += 1

print(ans)

