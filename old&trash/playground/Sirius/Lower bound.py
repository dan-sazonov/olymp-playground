n = int(input())
arr = list(map(int, input().split()))
m = int(input())
asks = list(map(int, input().split()))


def lower_bound(x):
    left = -1
    right = n
    while right - left > 1:
        m = (right + left) // 2
        if arr[m] < x:
            left = m
        else:
            right = m
    return right


arr.sort()
ans = [lower_bound(i) for i in asks]
print(*ans)
