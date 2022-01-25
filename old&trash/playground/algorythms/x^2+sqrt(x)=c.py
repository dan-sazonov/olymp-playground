c = int(input())
left = 0
right = c
for _ in range(200):
    m = (left + right) / 2
    if m ** 2 + m ** 0.5 < c:
        left = m
    else:
        right = m
print(right)
