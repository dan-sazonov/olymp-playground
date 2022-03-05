# (xy < A) ∨ (y > x) ∨ (x ≥ 8)

a = 1
while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((x * y < a) or (y > x) or (x >= 8)):
                break
        else:
            continue
        break
    else:
        print(a)
    a += 1
