def square_digits(num):
    foo = []
    for i in str(num):
        foo.append(str(int(i) ** 2))
    return int(''.join(foo))
