# Python 3.9.0
# Мы знаем, что gcd(a, b, c) = gcd(gcd(a,b), c). Исходя из этого нам нужно найти НОД двух первых чисел, а дальше
# записывать в эту переменную значение НОДа этой переменной и следующего числа. Для вычисления НОДа можно использовать
# итеративную реализацию алгоритма Евклида.
#
# Используя модуль math, код можно упростить до одной строки:
# from math import gcd
# print(gcd(*[int(input()) for _ in range(int(input()))]))


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input()) - 2
ans = gcd(int(input()), int(input()))

for _ in range(n):
    ans = gcd(ans, int(input()))

print(ans)
