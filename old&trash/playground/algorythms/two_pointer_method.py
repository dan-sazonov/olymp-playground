def amount(a, k):
    i = j = 0
    s = a[0]
    while True:
        if s == k:
            break
        elif s < k:
            if j == len(a) - 1:
                break
            j += 1
            s += a[j]
        else:
            s -= a[i]
            i += 1

    if s == k:
        print(i, j)
    else:
        print(-1, -1)

    return i, j


amount([1, 2, 3, 4], 5)  # 1 2
