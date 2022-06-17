def win1(x, s):
    return (x + 1 + s >= 67) or (x + s + s >= 67) or (x + x + s >= 67)


def loss1(x, s):
    return (not win1(x, s)) and win1(x + 1, s) and win1(x, s + 1) and win1(x + s, s) and win1(x, s + x)


def win2(x, s):
    return loss1(x + 1, s) or loss1(x, s + 1) or loss1(x + s, s) or loss1(x, s + x)


def loss12(x, s):
    return ((win1(x + 1, s) or win2(x + 1, s)) and (win1(x, s + 1) or win2(x, s + 1)) and
            (win1(x + s, s) or win2(x + s, s)) and (win1(x, s + x) or win2(x, s + x)))


x = 9
for s in range(1, 58):
    if loss12(x, s):
        print(s)
