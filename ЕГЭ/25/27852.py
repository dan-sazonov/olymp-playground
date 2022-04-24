for i in range(185311, 185331):
    tmp = []

    for j in range(1, i + 1):
        if i % j == 0:
            tmp.append(j)
        if len(tmp) > 4:
            break
    else:
        if len(tmp) == 4:
            print(*tmp)


