a, b, c = map(int, input().split())
d = b * b - (4 * a * c)

if d < 0 or a == 0:
    print(0)
elif d == 0:
    print(1)
else:
    print(2)
