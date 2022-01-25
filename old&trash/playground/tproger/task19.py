def foo (x, y):
    x, y = y, x
    return [x, y]

print(foo(1, 9))