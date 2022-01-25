ans, k = map(int, input().split())

for i in range(1, k + 1):
    ans += i if ans < i else -i

print(ans)
