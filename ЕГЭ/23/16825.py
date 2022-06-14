def f(x, end):
    if x > end or x == 6 or x == 12:
        return 0
    if x == end:
        return 1
    return f(x + 1, end) + f(x * 2, end) + f(x + 3, end)


print(f(3, 16))
