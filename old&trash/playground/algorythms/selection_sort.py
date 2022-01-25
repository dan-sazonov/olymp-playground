def selection(arr):
    for i in range(len(arr) - 1):
        imin = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[imin]:
                imin = j
        arr[imin], arr[i] = arr[i], arr[imin]
    return arr


print(selection([5, 2, 9, 3, 4]))
