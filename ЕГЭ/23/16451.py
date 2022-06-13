def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    return f(x + 1, end) + f(x * 2, end) + f(x + 3, end)


print(f(3, 12) * f(12, 16))
