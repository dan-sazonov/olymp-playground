a = int(input())
n = int(input())
ans = a + n

if a < 0 <= ans:
    ans += 1
elif a > 0 >= ans:
    ans -= 1

print(ans)
