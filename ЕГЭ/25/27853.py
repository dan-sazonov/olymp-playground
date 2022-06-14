ans = []

for i in range(312614, 312652):
    divs = {1, i}
    for j in range(2, i // 2 + 2):
        if i % j == 0:
            divs.add(j)

    if len(divs) == 6:
        ans.append(sorted(divs))

print(*ans)
