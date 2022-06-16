def win1(s):
    return (s + 1 >= 30) or (s * 3 >= 30)


for s in range(1, 30):
    if win1(s + 1) or win1(s * 3):
        print(s)
