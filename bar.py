from datetime import datetime

n = int(2 ** 20 - 1)
t = datetime.now()
hack = 1025025474013

sieve = list(range(n + 1))

for i in sieve:
    if i > 1:
        for j in range(i + i, len(sieve), i):
            sieve[j] = 0

print(datetime.now() - t)
print(*filter(lambda x: bool(x), sieve))
