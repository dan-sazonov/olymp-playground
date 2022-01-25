n = int(input())


def is_prime(x):
    if x % 2 == 0:
        return x == 2
    d = 3
    while d * d <= x and x % d != 0:
        d += 2
    return d * d > x


for i in range(2, n + 1):
    if is_prime(i):
        # print(i)
        for j in range(n + 1):
            # print('-',j,is_prime(j))
            if is_prime(j) and i + j == n:
                print(i, j)
                exit()
