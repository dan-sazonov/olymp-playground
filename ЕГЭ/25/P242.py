for i in range(1494999, 1403, -1):
    s = str(i)
    if i % 217 == 0 and s[:2] == '14' and s[3] == '4':
        print(i, i // 217)
