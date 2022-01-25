import math

a, b, c = map(int, input().split())
ans = []


def gcd_ext(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = gcd_ext(b, a % b)
    x, y = y, x - (a // b) * y
    return d, x, y


d, x0, y0 = gcd_ext(a, b)
if c % d != 0:
    print(-1)
t = ((c / d) * x0) / (-(b / d))
solve = math.floor(t), math.ceil(t)

for t in range(min(solve), max(solve) + 1):
    xi = ((c / d) * x0) + ((b / d) * t)
    yi = ((c / d) * y0) - ((a / d) * t)
    ans.append([xi, yi])

x_min = 0
for i in range(len(ans)):
    if 0 <= ans[i][0] > ans[x_min][0]:
        x_min = i
print(*map(int, ans[x_min]))
