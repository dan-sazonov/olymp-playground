def find_div(n):
    for i in range(18, n // 2 + 1):
        if i % 10 == 8 and n % i == 0:
            return i
    return 0


i = 500001
while True:
    d = find_div(i)
    if d:
        print(i, d)
    i += 1
