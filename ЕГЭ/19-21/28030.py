def win1(s):
    return (s + 1 >= 35) or (s + 2 >= 35) or (s * 2 >= 35)


for s in range(1, 35):
    if win1(s + 1) or win1(s + 2) or win1(s * 2):
        print(s)
