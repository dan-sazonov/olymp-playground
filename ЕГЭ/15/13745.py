# ((x ≤ 9) →(x ⋅ x ≤ A)) ⋀ ((y ⋅ y ≤ A) → (y ≤ 9))= 1

a = 0
while True:
    check = 1
    for x in range(100):
        for y in range(100):
            if not (((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9))):
                check = 0
    if check:
        print(a)
    a += 1
