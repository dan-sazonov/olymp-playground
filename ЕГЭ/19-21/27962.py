def win1(s):
    return (s + 1 >= 48) or (s + 3 >= 48) or (s * 2 >= 48)


for s in range(1, 48):
    if win1(s + 1) or win1(s + 3) or win1(s * 2):
        print(s)
