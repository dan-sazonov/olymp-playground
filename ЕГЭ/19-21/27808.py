def win1(s):
    return (s + 1 >= 42) or (s + 3 >= 42) or (s * 2 >= 42)


for s in range(1, 42):
    if win1(s + 1) or win1(s + 3) or win1(s * 2):
        print(s)
