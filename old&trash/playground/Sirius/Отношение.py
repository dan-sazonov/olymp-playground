n = int(input())
arr = list(map(int, input().split()))
i_best = j_best = i_min = 0

for j in range(2, len(arr)):
    if arr[j-1] < arr[i_min]:
        i_min = j - 1
    if arr[j] / arr[i_min] > arr[j_best] - arr[i_best]:
        if arr[j] / arr[i_min] > 1:
            j_best = j
            i_best = i_min

print(i_best + 1, j_best + 1)
