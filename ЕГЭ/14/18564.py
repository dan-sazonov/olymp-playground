def f(x, a, b):
    x = int(str(x), a)
    s = ''
    while x > 0:
        s += str(x % b)
        x //= b
    return s[::-1]


for i in range(10, 100):
    if hex(i)[-1] == 'b' and f(i, 10, 5)[-1] == '3':
        print(i)
