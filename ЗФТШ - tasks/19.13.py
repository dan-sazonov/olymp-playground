from math import sqrt

n = int(input())
s1 = 0

for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        s1 += (n // i + i) if i != sqrt(n) else i

print(s1)
