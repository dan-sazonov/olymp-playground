n, x, y = map(int, input().split())
left = 0
right = (n - 1) * max(x, y)

while right > left + 1:
    m = (right + left) // 2
    if m // x + m // y >= n - 1:
        right = m
    else:
        left = m

print(right + min(x, y))
