# F(1) = 3
#
# F(n) = F(n–1) * (n–1), при n >1
#
# Чему равно значение функции F(6)?

def f(n):
    if n == 1:
        return 3
    if n > 1:
        return f(n - 1) * (n - 1)


print(f(6))
