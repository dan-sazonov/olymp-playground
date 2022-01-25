n = int(input())
ans = [0] * n
ans[0] = 3  # a1

if n > 1:
    ans[1] = 8  # a2
    for i in range(2, n):
        ans[i] = (ans[i-1] + ans[i-2]) * 2

print(ans[-1])
