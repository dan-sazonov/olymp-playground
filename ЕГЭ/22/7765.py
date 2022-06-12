def f(x):
    a, b = 0, 10
    while x > 0:
        y = x % 10
        x //= 10
        if y > a:
            a = y
        if y < b:
            b = y
    return a, b


i = 100_00
while i <= 999_99:
    if f(i) == (6, 3):
        print(i)
        break
    i += 1
