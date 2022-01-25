def foo(n):
    ans = 0
    for c in list(str(abs(n))):
        ans += int(c)
    return ans

print(foo(int(input())))