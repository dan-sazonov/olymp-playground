# x&51 = 0 ∨ (x&41 = 0 → x&А = 0)

a = 0
while True:
    for x in range(100_000):
        if not ((x & 51 == 0) and ((x & 41 == 0) <= (x & a == 0))):
            break
    else:
        print(a)
    a += 1
