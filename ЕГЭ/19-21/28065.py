def win1(s):
    return (s + 1 >= 39) or (s + 2 >= 39) or (s * 2 >= 39)


def loss1(s):
    return not win1(s) and win1(s + 1) and win1(s + 2) and win1(s * 2)


def win2(s):
    return loss1(s + 1) or loss1(s + 2) or loss1(s * 2)


for s in range(1, 38):
    if win2(s):
        print(s)
