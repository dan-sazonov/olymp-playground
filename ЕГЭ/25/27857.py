m = 0
jm = 0


def foo(n):
    ans = 1
    for i in range(1, n//2+1):
        if n % i == 0:
            ans += 1
    return ans


# for i in range(2, 49):
for i in range(84052, 84130):
    t = foo(i)
    if t > m:
        m = t
        jm = i

print(m, jm)
