def win1(x, s):
    return (x + 1 + s >= 82) or (x * 4 + s >= 82) or (x + s * 4 >= 82)


def loss1(x, s):
    return (not win1(x, s)) and win1(x + 1, s) and win1(x * 4, s) and win1(x, s + 1) and win1(x, s * 4)


def win2(x, s):
    return loss1(x + 1, s) or loss1(x * 4, s) or loss1(x, s + 1) or loss1(x, s * 4)


def loss12(x, s):
    return ((win1(x + 1, s) or win2(x + 1, s)) and (win1(x * 4, s) or win2(x * 4, s)) and
            (win1(x, s + 1) or win2(x, s + 1)) and (win1(x, s * 4) or win2(x, s * 4)))


x = 4
for s in range(1, 78):
    if loss12(x, s):
        print(s)
