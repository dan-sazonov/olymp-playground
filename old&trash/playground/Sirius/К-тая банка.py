n, k = map(int, input().split())
a = list(map(int, input().split()))


def qsort(a):
    if len(a) < 2:
        return a
    else:
        pivot = a[0]
        less = [i for i in a[1:] if i <= pivot]
        greater = [j for j in a[1:] if j > pivot]
        return qsort(less) + [pivot] + qsort(greater)


print(qsort(a)[k - 1])
