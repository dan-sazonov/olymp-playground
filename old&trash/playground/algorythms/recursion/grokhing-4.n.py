arr = [7, 5, 76, 5, 6, 6,2, 3,0]


def sum_arr(arr):
    if not arr:
        return 0
    return arr[0] + sum_arr(arr[1:])


def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])


def count_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = count_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


def test(arr):
    if not arr:
        return 0
    x = arr[1:]
    print(x)
    return 1 + test(arr[1:])


def qsort(arr):
    if len(arr) < 2:
        print(arr)
        return arr
    else:
        pivot = arr[0]
        print(pivot)
        less_than_pivot = [i for i in arr[1:] if i <= pivot]
        print(less_than_pivot)
        greater_than_pivot = [i for i in arr[1:] if i > pivot]
        print(greater_than_pivot)
    print('=======')
    return qsort(less_than_pivot) + [pivot] + qsort(greater_than_pivot)


print(qsort(arr))
