a = list(map(int, input().split()))
n = len(a)
unordered = True
iter_counter = 0

while unordered:
    iter_counter += 1
    unordered = False
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            unordered = True
    n -= 1

print(iter_counter)
