n = int(input())
arr = sorted(list(input().split()))
m = int(input())
asks = list(input().split())
ans = []

for x in asks:
    left = -1
    right = n
    while right - left > 1:
        m = (right + left) // 2
        if arr[m] <= x:
            left = m
        else:
            right = m
    ans.append(right)

print(*ans)
