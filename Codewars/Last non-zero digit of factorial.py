dig = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]


def get_last_number(n):
    if n < 10:
        return dig[n]

    if ((n // 10) % 10) % 2 == 0:
        return (6 * get_last_number(n // 5) * dig[n % 10]) % 10

    else:
        return (4 * get_last_number(n // 5) * dig[n % 10]) % 10


def last_digit(n):
    return get_last_number(n)
