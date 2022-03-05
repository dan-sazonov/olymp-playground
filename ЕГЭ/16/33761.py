# F(0) = 0;
#
# F(n) = F(n / 2), если
# n > 0
# и
# при
# этом
# n
# чётно;
#
# F(n) = 1 + F(n − 1), если
# n
# нечётно.
#
# Назовите
# минимальное
# значение
# n, для
# которого
# F(n) = 11.


def f(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return f(n / 2)
    elif n % 2 != 0:
        return 1 + f(n - 1)


for i in range(0, 111234123341112341233411123412334):
    if f(i) == 11:
        print(i)
        break
