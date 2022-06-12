def f(x):
    a = 0
    b = 0
    while x > 0:
        if x % 2 > 0:
            a += 1
        else:
            b += x % 6
        x = x // 6
    return a, b


x = 0
while True:
    if f(x) == (2, 6):
        print(x)
        break
    x += 1
