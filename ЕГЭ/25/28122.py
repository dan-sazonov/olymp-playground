def find_divs(n):
    ans = []
    for i in range(1, n+1):
        if n % i == 0:
            ans.append(i)
        if len(ans) > 4:
            break
    return ans


for i in range(489421, 489441):
    n = find_divs(i)
    if len(n) == 4:
        print(*n)
