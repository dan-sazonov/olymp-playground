n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(len(a) - 1):
    i_max = i
    for j in range(i + 1, len(a)):
        if a[j] > a[i_max]:
            i_max = j
    a[i_max], a[i] = a[i], a[i_max]

    if i == (n - k):
        print(a[i])
        break
else:
    print(a[i + 1])
