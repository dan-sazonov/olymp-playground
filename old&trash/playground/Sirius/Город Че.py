n, r = map(int, input().split())
res = 0
arr = list(map(int, input().split()))
i = 0
j = 1

while i < len(arr) - 1 and j < len(arr):
    if arr[j] - arr[i] <= r:
        j += 1
    else:
        res += n - j
        i += 1

print(res)
