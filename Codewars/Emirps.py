def emirps(n):
    a = list(range(0, n + 1))
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i * 2
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1

    a = set(a)
    a.remove(0)
    # создать множество с простыми
    # исключить из результата общие элементы в обеих множествах
    tmp = set(map(lambda x: int(str(x)[::-1]), a))
    print(a, tmp, sep='\n')
    print((a - tmp), (tmp - a))


print(emirps(50))
