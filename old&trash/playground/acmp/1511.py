a = int(input())
b = int(input())
c = int(input())
m = 0
left = 0
right = 10 ** 15

while left < right:
    m = (right + left) // 2
    if (2 * a + 3 * b + 4 * c + 5 * m) / (a + b + c + m) < 3.5:
        left = m + 1
    else:
        right = m

print(m)
