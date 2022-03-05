def F(n):
    if n > 0:
        F(n - 3)
        F(n // 3)
        print(n, sep='', end='')


F(9)
