# F(1) = 1
#
# F(n) = F(n–1) + 2n–1 , если n > 1.
#
# Чему равно значение функции F(12)?

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + 2 ** (n - 1)


print(f(12))
