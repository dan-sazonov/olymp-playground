n = int(input())
i = 1
ans = 0

while i <= n:
    if n % i == 0:
        ans += i
    i += 1

print(ans)
