def f(x):
    Q = 9
    L = 0
    while x >= Q:
        L = L + 1
        x = x - Q
    M = x
    if M < L:
        M = L
        L = x
    return L, M


x = 0
while True:
    if f(x) == (4, 5):
        print(x)
    x += 1
