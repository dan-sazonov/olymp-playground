m = int(input())
n = int(input())
arr = set(input() for i in range(m))
ans = []

for _ in range(n):
    if input() in arr:
        ans.append('YES')
    else:
        ans.append('NO')

print(*ans, sep='\n')
