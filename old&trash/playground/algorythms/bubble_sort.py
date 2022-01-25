def bubble_sort(arr):
    n = len(arr)
    unordered = True

    while unordered:
        unordered = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                unordered = True
        n -= 1

    return arr


print(bubble_sort([5, 2, 9, 3, 4]))
