def merge(a, b):
    res = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    res.extend(a[i:])
    res.extend(b[j:])

    return res


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    k = len(arr) // 2
    return merge(merge_sort(arr[k:]), merge_sort(arr[:k]))


print(merge_sort([5, 2, 9, 3, 4]))
