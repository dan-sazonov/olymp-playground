def foo(n):
    ans = []
    for j in range(2, n//2+1):
        if n % j == 0:
            ans.append(j)
        if len(ans) > 3:
            break
    return ans


for i in range(123456789, 223456790):
    print(i)
    t = foo(i)
    if len(t) == 3:
        print(i, t[-1])
