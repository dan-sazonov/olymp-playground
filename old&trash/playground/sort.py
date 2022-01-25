# FIXME quicksort
# FIXME selection sort

# TODO mergesort
# TODO bubble sort
# TODO heapsort
# TODO insertion sort
# TODO tree sort
# TODO timsort


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr if x <= pivot]
        greater = [x for x in arr if x > pivot]
    return quicksort(less) + quicksort(greater)


def selection_sort(arr):
    for i in range(len(arr) - 1):
        pivot = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[pivot]:
                pivot = j
        arr[i], arr[pivot] = arr[pivot], arr[i]
    return arr
