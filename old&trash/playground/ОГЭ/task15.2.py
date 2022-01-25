foo = input().split()


def iteration(foo):
    bar = 0
    for c in foo[1:]:
        if c[-1] == '2' and int(c) > bar:
            bar = int(c)
        else:
            continue
    return bar


print(iteration(foo))
