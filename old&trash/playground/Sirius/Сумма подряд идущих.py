n, k, m = map(int, input().split())
arr = list(map(int, input().split()))
total = sum(arr[:k + 1])

if total != m:
    for i in range(1, n - k):
        total += arr[i + k] - arr[i - 1]
        if total == m:
            break
    print(i + 1)
else:
    print(1)
