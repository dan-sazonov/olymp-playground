# x & 73 = 0 → (x & 28 ≠ 0 → x & А ≠ 0)

a = 0
while True:
    for x in range(1_000_000):
        if not ((x & 73 == 0) <= ((x & 28 != 0) <= (x & a != 0))):
            break
    else:
        print(a)
    a += 1
