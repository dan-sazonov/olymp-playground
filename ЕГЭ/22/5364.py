def f(x):
    a = 0
    b = 0
    while x > 0:
        c = x % 2
        if c == 0:
            a += 1
        else:
            b += 1
        x = x // 10
    return a,b


x = 0
while True:
    if f(x) == (3,2):
        print(x)