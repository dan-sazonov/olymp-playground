n = int(input())
arr = list(map(int, input().split()))
i_max = 0
ans = 0
i_ans = 0

for i in range(n):
    if arr[i] > arr[i_max]:
        i_max = i

for j in range(i_max, n - 1):
    if arr[j] % 10 == 5 and arr[j + 1] <= arr[j] and arr[j] > ans:
        i_ans = j
        ans = arr[j]

print(i_ans + 1 if ans else ans)
