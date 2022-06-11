# F(1) = 1; F(2) = 1;
#
# F(n) = F(n - 2) * (n - 1), при n > 2.

def f(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return f(n - 2) * (n - 1)


print(f(8))
