import math

n, m = map(int, input().split())
q = math.gcd(n, m)

if m % n == 0:
    ans = 1
else:
    ans = int(n // q)

print(ans)
