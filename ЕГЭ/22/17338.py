def f(x):
    a = 0
    b = 10
    while x > 0:
        d = x % 6
        if d > a:
            a = d
        if d < b:
            b = d
        x = x // 6
    return a + b


x = 1
while True:
    if f(x) == 7:
        print(x)
        break
    x += 1
