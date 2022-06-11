def f(num, from_base, to_base):
    sl = ['a','b','c','d','e','f','g','h','j','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    len(sl)
    num = int(str(num), from_base)
    s = ''
    while num > 0:
        tmp = str(num % to_base)
        if int(tmp) > 10:
            tmp += sl[10 - int(tmp)]
        else:
            s += tmp
        num //= to_base
    return s[::-1]


for i in range(2,36):
    s = f(87, 10, i)
    print(i,s)
    if len(s) == 2 and s[-1] == 2:
        print(s)
