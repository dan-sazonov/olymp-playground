a = int(input())
b = int(input())
n = 1


def factorization(n):
    p = dict()
    d = 2
    while d * d <= n:
        while n % d == 0:
            p[d] = p.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        p[n] = p.get(n, 0) + 1
    return p


a_factorized = factorization(a)
b_factorized = factorization(b)

for key in a_factorized:
    if key not in b_factorized:
        n = -1
        break
    k = -(-a_factorized[key] // b_factorized[key])
    if k > n:
        n = k

print(n)
