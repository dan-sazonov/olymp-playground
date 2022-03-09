def f(x):
    a, b = 0, 0
    while x > 0:
        a = a + 1
        b = b + x % 100
        x = x // 100
    return a, b


x = 0
while True:
    x+=1
    if f(x) == (2, 13):
        print(x)
        break
