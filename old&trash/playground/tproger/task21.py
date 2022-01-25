foo = [1, 3, 5, 7, 7]


def spam(foo):
    foo.sort()
    bar = list(set(foo))
    bar.sort()
    return foo == bar


# правильное решение
def all_unique(numbers):
    return len(numbers) == len(set(numbers))


print(spam(foo))
