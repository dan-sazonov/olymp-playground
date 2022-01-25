def max_diff(a):
    i_best = 0
    j_best = 1
    i_min = 0

    for j in range(2, len(a)):
        if a[j - 1] < a[i_min]:
            i_min = j - 1
        if a[j] - a[i_min] > a[j_best] - a[i_best]:
            j_best = j
            i_best = i_min
    return i_best, j_best
