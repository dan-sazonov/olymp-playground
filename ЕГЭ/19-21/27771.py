def win1(x, s):
    return (x - 1 + s <= 20) or (x // 2 + s <= 20) or (x + s // 2 <= 20)


def loss1(x, s):
    return (not win1(x, s)) and win1(x - 1, s) and win1(x, s - 1) and win1(x // 2, s) and win1(x, s // 2)


def win2(x, s):
    return loss1(x - 1, s) or loss1(x, s - 1) or loss1(x // 2, s) or loss1(x, s // 2)


def loss12(x, s):
    return ((win1(x - 1, s) or win2(x - 1, s)) and (win1(x, s - 1) or win2(x, s - 1)) and
            (win1(x // 2, s) or win2(x // 2, s)) and (win1(x, s // 2) or win2(x, s // 2)) and
            (win2(x - 1, s) or win2(x, s - 1) or win2(x // 2, s) or win2(x, s // 2)))


x = 10
for s in range(11, 200):
    if loss12(x, s):
        print(s)
