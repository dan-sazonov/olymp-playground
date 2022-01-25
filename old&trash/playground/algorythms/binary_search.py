def ok(n):
    pass


def search(l, r):
    while r - l > 1:
        m = (r + l) // 2
        if ok(m):
            l = m
        else:
            r = m
    return l, r


def lower_bound(a, x):
    left = -1
    right = len(a)
    while right - left > 1:
        m = (right + left) // 2
        if a[m] < x:
            left = m
        else:
            right = m
    if right < len(a) and a[right] == x:
        return right
    return -1


def upper_bound(a, x):
    left = -1
    right = len(a)
    while right - left > 1:
        m = (right + left)
        if a[m] <= x:
            left = m
        else:
            right = m
    if left < len(a) and a[left] == x:
        return right
    return -1


a = [1, 2, 3, 4, 4, 4, 5, 6, 9]
x = 4
print(lower_bound(a, x))
print(upper_bound(a, x))
