def fib_true(n):
    F = [0] * (n + 1)
    F[0] = 1
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 2] + F[i - 1]
    print(F[-1])


def fib(n):
    a = 1
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_3_true(n):
    F = [0] * (n + 1)
    F[0] = 1
    F[1] = F[0]
    F[2] = F[1] + F[0]
    for i in range(3, n + 1):
        F[i] = F[i - 3] + F[i - 2] + F[i - 1]
    print(F[-1])


def fib_3_true_b(n):
    F = [0] * (n + 1)
    F[0] = 1
    F[1] = F[0]
    F[2] = F[1] + F[0]
    for i in range(3, n + 1):
        F[i] = sum(F[max(0, i - 3): i])
    print(F[-1])


def fib_3(n):
    a = 1
    b = 1
    c = b + a
    for _ in range(n):
        a, b, c = c, a + b, b + c
    return a, b, c


price = [1, 6, 7, 5, 3, 4, 5]


def fib_w_cost_true(n):
    coast = [0] * (n + 1)
    coast[1] = price[1]
    for i in range(2, n + 1):
        coast[i] = min(coast[i - 1], coast[i - 2]) + price[i]
    return coast


def fib_w_cost(n):
    a = 0
    b = price[1]
    for i in range(2, n + 1):
        a, b = b, min(a, b) + price[i]
    return a, b


x = int(input())
print(fib_w_cost_true(x))
print(fib_w_cost(x))
