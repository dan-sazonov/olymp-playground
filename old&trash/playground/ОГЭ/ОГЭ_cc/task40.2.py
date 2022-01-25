num = int(input())
ans = 0

while num > 0:
    temp = int(input())
    ans += temp if temp % 6 == 0 else 0
    num -= 1

print(ans)
