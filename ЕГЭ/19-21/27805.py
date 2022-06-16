def win1(s):
    return (s + 1 >= 63) or (s + 4 >= 63) or (s * 5 >= 63)


def loss1(s):
    return not (win1(s)) and win1(s + 1) and win1(s + 4) and win1(s * 5)


def win2(s):
    return loss1(s + 1) or loss1(s + 4) or loss1(s * 5)


for s in range(1, 63):
    if win2(s):
        print(s)
