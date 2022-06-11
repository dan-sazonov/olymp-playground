# (5x + 3y ≠ 60) ∨ ((A > x) ∧ (A > y)) = 1

a = 0
while True:
    check = 1
    for x in range(100):
        for y in range(100):
            if not ((5 * x + 3 * y != 60) or ((a > x) and (a > y))):
                check = 0
    if check:
        print(a)
        break
    a += 1
