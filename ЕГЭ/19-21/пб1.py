def win1(s):
    return (s + 3 >= 56) or (s * 2 >= 56)


def loss1(s):
    return (not win1(s)) and win1(s + 3) and win1(s * 2)


def win2(s):
    return loss1(s + 3) or loss1(s * 2)


def loss12(s):
    return (win1(s + 3) or win2(s + 3)) and (win1(s * 2) or win2(s * 2))


for s in range(1, 53):
    if loss12(s):
        print(s)
