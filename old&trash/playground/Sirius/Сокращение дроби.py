import math

a, b = map(int, input().split())
n = math.gcd(a, b)
print(a//n, b//n)
