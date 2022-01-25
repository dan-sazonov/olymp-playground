def insertion_sort(arr):
    for i in range(1, len(arr)):
        pivot = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > pivot:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = pivot
    return arr


print(insertion_sort([5, 2, 9, 3, 4]))
