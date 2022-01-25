n = int(input())
base = []
top = [0]

for _ in range(n):
    x, y = map(int, input().split())
    if y == 0:
        base.append(x)
    else:
        top.append(y)

a = max(base) - min(base)
h = max(top)
if base:
    print(round(a / 2 * h))
else:
    print(0)
