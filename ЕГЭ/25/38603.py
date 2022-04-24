def find_m(n):
    m = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            m += i
            break
    for i in range(n // 2 + 1, 2, -1):
        if n % i == 0:
            m += i
            break
    return m


i = 700_001
while True:
    m = find_m(i)
    if m % 10 == 8:
        print(i, m)
    i += 1
