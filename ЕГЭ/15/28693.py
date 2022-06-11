# (2x + 3y < A) ∨ (x > y) ∨ (y > 24) = 1

a = 0
while True:
    check = 1
    for x in range(100):
        for y in range(100):
            if not ((2 * x + 3 * y < a) or (x > y) or (y > 24)):
                check = 0
    if check:
        print(a)
        break
    a += 1
