def find_m(n):
    s = 0
    c = 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            s += i
            c += 1
            break
    for i in range(n // 2 + 1, 2, -1):
        if n % i == 0:
            s += i
            c += 1
            break
    return s if c == 2 else 0


i = 452022
while True:
    m = find_m(i)
    if m % 7 == 3:
        print(i, m)
    i += 1