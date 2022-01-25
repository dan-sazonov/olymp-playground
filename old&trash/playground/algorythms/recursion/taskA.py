bar = []
def counter(foo):
    if foo == 1:
        print(1)
    else:
        print(counter(foo - 1))


print(counter(10))