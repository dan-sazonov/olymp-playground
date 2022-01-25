def check(c=0):

    a = int(input())
    b = int(input())
    ta = a + 10 - (a % 10)
    tb = b - (b % 10)
    ans = (tb - ta) // 2
    for i in range(a, ta):
        ans += check(i)
    for i in range(tb, b + 1):
        ans += check(i)
    print(ans)


check()