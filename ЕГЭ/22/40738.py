def f(x):
    a = 1
    b = 0
    while x > 0:
        d = x % 9
        a *= d
        if d < 5:
            b += d
        x //= 9
    return a, b


x = 0
while True:
    x += 1
    if f(x) == (10, 9):
        print(x)
