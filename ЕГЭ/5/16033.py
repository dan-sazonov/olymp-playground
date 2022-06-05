def f(n):
    s = bin(n)
    if n % 2 ==0:
        s += '01'
    else:
        s += '10'
    return int(s,2)


n = 0
while True:
    r = f(n)
    if r > 102:
        print(r)
        break

    n += 1
