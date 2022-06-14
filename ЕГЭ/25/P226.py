def f(st):
    for i in range(len(st) - 1):
        if not (st[i + 1] > st[i]):
            return False
    return True


for i in range(159, 1_234_567_89 + 1):
    s = str(i)
    if f(s) and s[0] == '1' and s[-1] == '9' and '5' in s and i % 21 == 0:
        print(i, i // 21)
