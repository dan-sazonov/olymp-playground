def f(n):
    pr = n
    n = bin(n)[2:]
    if pr % 2 == 0:
        return int(f'10{n}', 2)
    return int(f'1{n}01', 2)


n = 0
while True:
    r = f(n)
    if r > 441:
        print(n)
        break
    n += 1
