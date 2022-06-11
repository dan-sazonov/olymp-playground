# (x > A) ∨ (y > A) ∨ (2y + x < 110) = 1

a = 0
while True:
    check = 1
    for x in range(100):
        for y in range(100):
            if not ((x > a) or (y > a) or (2 * y + x < 110)):
                check = 0
    if check:
        print(a)
    a += 1
