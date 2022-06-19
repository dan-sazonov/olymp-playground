def f(n):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = f'{s}10'
    else:
        s = f'1{s}01'

    return int(s, 2)


n = 0
while True:
    if f(n) > 516:
        print(n)
        break
    n += 1
