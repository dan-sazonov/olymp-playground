def win1(x, s):
    return (x + s + 1 >= 45) or (x * 3 + s >= 45) or (x + s * 3 >= 45)


def loss1(x, s):
    return (not win1(x, s)) and win1(x + 1, s) and win1(x, s + 1) and win1(x * 3, s) and win1(x, s * 3)


def win2(x, s):
    return loss1(x + 1, s) or loss1(x, s + 1) or loss1(x * 3, s) or loss1(x, s * 3)


def loss12(x, s):
    return ((win1(x + 1, s) or win2(x + 1, s)) and (win1(x, s + 1) or win2(x, s + 1)) and
            (win1(x * 3, s) or win2(x * 3, s)) and (win1(x, s * 3) or win2(x, s * 3)))


x = 4
for s in range(1, 41):
    if win2(x, s):
        print(s)
