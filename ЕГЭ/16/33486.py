# F(0) = 0;
#
# F(n) = n + F(n − 3), если n mod 3 = 0, и n > 0;
#
# F(n) = n + F(n − (n mod 3)), если n mod 3 > 0.

def f(n):
    if n == 0:
        return 0
    if n % 3 == 0 and n > 0:
        return n + f(n - 3)
    if n % 3 > 0:
        return n + f(n - (n % 3))


print(f(26))
