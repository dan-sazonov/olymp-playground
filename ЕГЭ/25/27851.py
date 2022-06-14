ans = []

for i in range(210235, 210301):
    divs = set()
    for j in range(2, i // 2 + 2):
        if i % j == 0:
            divs.add(j)

    if len(divs) == 4:
        ans.append(sorted(divs))

print(*ans)
