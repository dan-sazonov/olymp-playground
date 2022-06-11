# (y + 2x < A) ∨ (x > 30) ∨ (y > 20) == 1

a = 0

while True:
    check = 1
    for x in range(1000):
        for y in range(1000):
            if not (((y + 2*x) < a) or (x>30) or (y>20)):
                check = 0
    if check:
        print(a)
    a += 1
