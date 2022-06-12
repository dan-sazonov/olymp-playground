# x & 85 = 0 → (x & 54 ≠ 0 → x & А ≠ 0)

a = 0
while True:
    for x in range(1000):
        if not ((x & 85 == 0) <= ((x & 54 != 0) <= (x & a != 0))):
            break
    else:
        print(a)
        break
    a += 1
