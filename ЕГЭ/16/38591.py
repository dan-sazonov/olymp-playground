# F(n) = 1 при n = 1;
#
# F(n) = n + F(n − 1), если n чётно,
#
# F(n) = 2 × F(n − 2), если n > 1 и при этом n нечётно.
#
# Чему равно значение функции F(26)?

def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + f(n - 1)
    elif n > 1 and n % 2 != 0:
        return 2 * f(n - 2)


print(f(26))
