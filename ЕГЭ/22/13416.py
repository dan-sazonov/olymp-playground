def f(x):
    a = b = 0
    while x > 0:
        a += 1
        if x % 2 == 0:
            b += x % 10
        x //= 10
    return a, b


x = 0
while True:
    if f(x) == (3, 14):
        print(x)
        break
    x += 1
