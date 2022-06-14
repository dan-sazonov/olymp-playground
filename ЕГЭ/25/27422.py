ans = []
for i in range(174457, 174506):
    divs = set()
    for j in range(2, i // 2 + 2):
        if i % j == 0:
            divs.add(j)
    if len(divs) == 2:
        ans.append(sorted(divs))

print(*ans, sep='\n')
