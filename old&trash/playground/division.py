from math import sqrt


# TODO зафигачить консольный интерфейс


def find_div(n):
    divisor = [1, n]
    for i in range(2, n):
        if n % i == 0:
            divisor.insert(-1, i)
    return divisor


def is_prime(n):
    return len(find_div(n)) > 2


def is_prime_fast(n):
    if n == 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_stream(n=0):
    # TODO ловить KeyboardInterrupt
    if n:
        for i in range(2, abs(n) + 1):
            if is_prime_fast(i):
                print(i)
    else:
        n = 2
        while True:
            if is_prime_fast(n):
                print(n)
            n += 1


def find_prime(n):
    prime = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime


def eratosthenes(n):
    a = list(range(0, n + 1))
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i * 2
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1

    a = set(a)
    a.remove(0)
    return a


def is_prime_root(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


print(eratosthenes(20))
