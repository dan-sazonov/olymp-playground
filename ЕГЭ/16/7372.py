# F(n) = 1 при n = 1;
#
# F(n) = F(n − 1) · n при n ≥ 2.
#
# Чему равно значение функции F(6)?


def f(n):
    if n == 1:
        return 1
    elif n >= 2:
        return f(n - 1) * n


print(f(6))
