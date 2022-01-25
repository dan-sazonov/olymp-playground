k = int(input())
m = int(input())
a = int(input())
b = int(input())
ans = 0

for i in range(a, b + 1):
    if i % k == 0:
        ans += 1
    if i % m == 0:
        ans -= 1

print(ans)
