a, b = map(int, input().split())
prime = [True] * (b + 1)
prime[0] = prime[1] = False
ans = set(range(2, b + 1))
res = set()

for i in range(2, b + 1):
    if not prime[i]:
        continue
    for j in range(i * i, b + 1, i):
        prime[j] = False
        if j in ans:
            ans.remove(j)

for c in ans:
    for d in ans:
        tmp = c + d
        if a <= tmp <= b:
            res.add(tmp)

print(*sorted(res), sep='\n')
