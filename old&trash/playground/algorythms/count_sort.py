def count_sort(arr):
    res = [0] * (max(arr) + 1)
    ans = []

    for i in arr:
        res[i] += 1

    for j in range(len(res)):
        ans += [j] * res[j]

    return ans


print(count_sort([5, 2, 9, 3, 4]))
