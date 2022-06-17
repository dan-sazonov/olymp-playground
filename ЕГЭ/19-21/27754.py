def win1(x, s):
    return (x + s + 1 >= 61) or (x * 4 + s >= 61) or (x + s * 4 >= 61)


def loss1(x, s):
    return (not win1(x, s)) and win1(x, s + 1) and win1(x, s * 4) and win1(x + 1, s) and win1(x * 4, s)


def win2(x, s):
    return loss1(x, s + 1) or loss1(x, s * 4) or loss1(x + 1, s) or loss1(x * 4, s)


def loss12(x, s):
    return ((win1(x, s + 1) or win2(x, s + 1)) and (win1(x, s * 4) or win2(x, s * 4)) and
            (win1(x + 1, s) or win2(x + 1, s)) and (win1(x * 4, s) or win2(x * 4, s)))


x = 3
for s in range(1, 58):
    if loss12(x, s):
        print(s)
