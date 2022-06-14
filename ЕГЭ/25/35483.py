ans = []

for i in range(35_000_000, 40_000_000):
    divs = set()
    if i % 2 != 0:
        divs.add(i)

    for j in range(1, i//2+2,2):
        if i % j == 0:
            divs.add(j)
        if len(divs) > 5:
            break
    if len(divs) == 5:
        ans.append(sorted(divs))
        print(ans)