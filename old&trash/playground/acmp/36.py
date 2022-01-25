n = int(input())
counter = 0


def is_prime(x):
    if x % 2 == 0:
        return x == 2
    d = 3
    while d * d <= x and x % d != 0:
        d += 2
    return d * d > x


for i in range(n + 1, 2 * n):
    counter += is_prime(i)

print(counter)
