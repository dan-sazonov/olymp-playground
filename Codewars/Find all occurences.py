def find_all(array, n):
    out = []
    for i in enumerate(array):
        if i[1] == n:
            out.append(i[0])
    return out
