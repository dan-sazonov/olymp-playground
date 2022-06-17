def win1(s):
    return (s + 1 >= 30) or (s * 3 >= 30)


def loss1(s):
    return not win1(s) and win1(s + 1) and win1(s * 3)


def win2(s):
    return loss1(s + 1) or loss1(s * 3)


def loss12(s):
    return (win1(s+1)or win2(s+1)) and (win1(s*3)or win2(s*3))


for s in range(1, 30):
    if loss12(s):
        print(s)
