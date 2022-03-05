# F(1) = 1
#
# F(n) = 2 * G(n–1) + 5 * n, при n >1
#
# G(1) = 1
#
# G(n) = F(n–1) + 2 * n, при n >1
#
# Чему равно значение функции F(4) + G(4)?


def g(n):
    if n == 1:
        return 1
    elif n > 1:
        return f(n - 1) + 2 * n


def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return 2 * g(n - 1) + 5 * n


print(f(4)+g(4))
