# F(1) = 1;
# F(2) = 2;
# F(3) = 3;
#
# F(n) = F(n − 3)*n
# при
# n > 3.
#
# Чему
# равно
# значение
# функции
# F(11)? В
# ответе
# запишите
# только
# натуральное
# число.


def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n > 3:
        return f(n - 3) * n


print(f(11))
