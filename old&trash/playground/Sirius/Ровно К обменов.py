n, k = map(int, input().split())
a = list(range(1, n + 1))
unordered = True

while unordered and k:
    unordered = False
    for i in range(len(a) - 1):
        if a[i] < a[i + 1] and k:
            a[i], a[i + 1] = a[i + 1], a[i]
            k -= 1
            unordered = True
    n -= 1

print(*a)
