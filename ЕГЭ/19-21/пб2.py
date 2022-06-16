def win1(s):
    return (s + 2 >= 60) or (s * 3 >= 60)


def loss1(s):
    return (not win1(s)) and win1(s + 2) and win1(s * 3)


def win2(s):
    return loss1(s + 2) or loss1(s * 3)


def loss12(s):
    return (win1(s+2) or win2(s+2)) and (win1(s*3) or win2(s*3))


for s in range(1, 59):
    if loss12(s):
        print(s)
