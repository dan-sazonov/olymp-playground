n = int(input())
a = list(map(int, input().split()))
unordered = True
swap_counter = 0

while unordered:
    unordered = False
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swap_counter += 1
            unordered = True
    n -= 1

print(a, swap_counter)
