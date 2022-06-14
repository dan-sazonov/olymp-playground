def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    return f(x + 1, end) + f(x * 3, end) + f(x + 2, end)


print(f(2, 9) * f(9, 11) * f(11, 12))
