# F(1) = 0
#
# F(n) = F(n–1) + n, при n >1
#
# G(1) = 1
#
# G(n) = G(n–1) * n, при n >1
#
# Чему равно значение функции F(5) + G(5)?


def f(n):
    if n == 1:
        return 0
    elif n > 1:
        return f(n - 1) + n


def g(n):
    if n == 1:
        return 1
    elif n > 1:
        return g(n - 1) * n


print(f(5) + g(5))
