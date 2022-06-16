def win1(s):
    return (s + 1 >= 35) or (s + 3 >= 35) or (s * 2 >= 35)


def loss1(s):
    return (not win1(s)) and win1(s + 1) and win1(s + 3) and win1(s * 2)


def win2(s):
    return loss1(s + 1) or loss1(s + 3) or loss1(s * 2)


def loss12(s):
    return (win1(s + 1) or win2(s + 1)) and (win1(s + 3) or win2(s + 3)) and (win1(s * 2) or win2(s * 2))


for s in range(1, 35):
    if loss12(s):
        print(s)
