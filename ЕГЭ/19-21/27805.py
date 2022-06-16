def win1(s):
    return (s + 1 >= 63) or (s + 4 >= 63) or (s * 5 >= 63)


for s in range(1, 63):
    if win1(s + 1) or win1(s + 4) or win1(s * 5):
        print(s)
