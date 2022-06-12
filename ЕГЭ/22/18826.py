def f(x):
    k, l = 9, 0
    while x >= k:
        l += 1
        x -= k
    m = x
    if m < l:
        m = l
        l = x
    return l, m


x = 0
while True:
    if f(x) == (5, 8):
        print(x)
        break
    x += 1
