from math import gcd

n = int(input())
x, y = map(int, input().split())
x0, y0 = x, y
tmp_x = tmp_y = 0
ans = 0

for i in range(n - 1):
    tmp_x, tmp_y = map(int, input().split())
    ans += gcd(abs(tmp_x - x0), abs(tmp_y - y0))
    x0, y0 = tmp_x, tmp_y

ans += gcd(abs(tmp_x - x), abs(tmp_y - y))
print(ans)
