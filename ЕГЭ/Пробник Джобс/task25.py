for i in range(10):
    for j in range(10):
        s = f'122345{i}6{j}8'
        n = int(s)
        if n % 17 == 0:
            print(n, n//17)
