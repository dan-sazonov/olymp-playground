def win1(x, s):
    return (x + s + 1 >= 77) or (x + s * 2 >= 77) or (x * 2 + s >= 77)


def loss1(x, s):
    return (not win1(x, s)) and win1(x, s + 1) and win1(x, s * 2) and win1(x * 2, s) and win1(x + 1, s)


def win2(x, s):
    return loss1(x, s + 1) or loss1(x, s * 2) or loss1(x * 2, s) or loss1(x + 1, s)


def loss12(x, s):
    return ((win1(x, s + 1) or win2(x, s + 1)) and (win1(x, s * 2) or win2(x, s * 2)) and
            (win1(x * 2, s) or win2(x * 2, s)) and (win1(x + 1, s) or win2(x + 1, s)))


x = 7
for s in range(1, 70):
    if loss12(x, s):
        print(s)
