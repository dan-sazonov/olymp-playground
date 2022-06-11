def f(num, from_base, to_base):
    num = int(str(num), from_base)
    s = ''
    while num > 0:
        s += str(num % to_base)
        num //= to_base
    return s[::-1]


for i in range(2,10):
    if len(f(50,10,i)) == 3:
        print(i)
