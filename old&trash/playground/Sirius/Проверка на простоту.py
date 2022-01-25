x = int(input())


def is_prime(n):
    if n % 2 == 0:
        return n == 2

    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


print('YES' if is_prime(x) else 'NO')
