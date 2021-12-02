m, n = map(int, input().split())
has_true = False

sieve = list(range(n + 1))
sieve[1] = 0
for i in sieve:
    if i > 1:
        for j in range(i + i, len(sieve), i):
            sieve[j] = 0

for i in sieve[m:]:
    if i:
        has_true = True
        print(i)

if not has_true:
    print('Absent')
