import collections


def rmq(a, k):
    res = []
    d = collections.deque()
    n = len(a)

    for i in range(n):
        if i >= k and d[0] == i - k:
            d.popleft()
        while len(d) and a[d[-1]] >= a[i]:
            d.pop()
        d.append(i)
        if i >= k - 1:
            res.append(a[d[0]])
    print(*res)
    return res


rmq([1, 3, 2, 4, 5, 3, 1], 3)
