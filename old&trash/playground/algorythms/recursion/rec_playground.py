
import sys

sys.setrecursionlimit(9000)


def q_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
    return q_sort(less) + [pivot] + q_sort(greater)


def builtins_sort(arr):
    return sorted(arr)


# for n in range(0, 950):
#     print(q_sort([x for x in range(0, n)]))
#     print(builtins_sort([x for x in range(0, n)]))

print(q_sort([x for x in range(0, 5000)]))
'''
sys.setrecursionlimit(5000)
limit = 1
while True:
    try:
        q_sort([n for n in range(0, limit, 20)])
        limit += 1
    except RecursionError:
        print(limit)
        break
'''
