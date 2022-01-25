def rec_pow(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 != 0:
        return a * rec_pow(a, n - 1)
    elif n % 2 == 0:
        return rec_pow(a * a, n / 2)


rec_pow(52536, 58519)

pow(52536, 58519)