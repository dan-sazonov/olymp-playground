def f(x, end):
    if x > end or x == 9:
        return 0
    if x == end:
        return 1
    return f(x + 1, end) + f(x * 2, end)


print(f(1, 10) * f(10, 20))  # 10 + 8
