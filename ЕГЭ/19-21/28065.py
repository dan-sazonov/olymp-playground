def win1(s):
    return (s + 1 >= 39) or (s + 2 >= 39) or (s * 2 >= 39)


for s in range(1, 38):
    if win1(s + 1) or win1(s + 2) or win1(s * 2):
        print(s)
