# F(1) = 1
#
# F(2) = 1
#
# F(3) = 1
#
# F(n) = F(n–3) + F(n–2), при n >3, где n – натуральное число.

def f(n):
    if n in {1, 2, 3}:
        return 1
    if n > 3:
        return f(n - 3) + f(n - 2)


print(f(12))
