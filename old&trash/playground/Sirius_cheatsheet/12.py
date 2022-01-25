a, k, b, m, x = 2, 4, 3, 3, 25

day = 0
while x > 0:
    if (day + 1) % b != 0:
        x -= a
    if (day + 1) % m != 0:
        x -= k
    day += 1

print(day)  # 7