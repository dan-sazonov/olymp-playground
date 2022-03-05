# (x * y < A) ∨ (x < y) ∨ (x ≥ 12)

a = 1
while True:
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((x * y < a) or (x < y) or (x >= 12)):
                break
        else:
            continue
        break
    else:
        print(a)
    a+=1
