def f(x, end):
    if x > end or x == 29:
        return 0
    if x == end:
        return 1
    return f(x + 1, end) + f(x * 2, end) + f(x * 3, end)


print(f(2, 13) * f(13, 44))
