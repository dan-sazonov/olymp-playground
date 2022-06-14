def f(x,end):
    if x > end or x == 24:
        return 0
    if x == end:
        return 1
    return f(x+1, end) + f(x*2+1, end)


print(f(1,25))
