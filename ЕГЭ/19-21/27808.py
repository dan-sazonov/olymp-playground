def win1(s):
    return (s + 1 >= 42) or (s + 3 >= 42) or (s * 2 >= 42)


def loss1(s):
    return not win1(s) and win1(s + 1) and win1(s + 3) and win1(s * 2)


def win2(s):
    return loss1(s + 1) or loss1(s + 3) or loss1(s * 2)


for s in range(1, 42):
    if win2(s):
        print(s)
