def f(x, end):
    if x > end or x == 13:
        return 0
    if x == end:
        return 1
    return f(x + 1, end) + f(x + 2, end) + f(x * 3, end)


print(f(1, 10) * f(10, 15))
