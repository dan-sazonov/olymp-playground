# x & 29 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)

a = 1
while True:
    for x in range(1, 1_000_000):
        if not ((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))):
            break
    else:
        print(a)
    a += 1
