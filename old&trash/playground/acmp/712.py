w, h, n = map(int, input().split())
left = 0
right = max(w*n, h*n)

while right - left > 1:
    m = (right + left) // 2
    if (m // w) * (m // h) >= n:
        right = m
    else:
        left = m

print(right)