k = int(input())
prime_counter = 0
i = 1
temp_prime = 1


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


while prime_counter <= k:
    if is_prime(i):
        temp_prime = i
        prime_counter += 1
    i += 1

print(temp_prime)
