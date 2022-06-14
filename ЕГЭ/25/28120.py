ans = []
for i in range(201455, 201470):
    divs = []
    for j in range(1, i // 2 + 2):
        if i % j == 0:
            divs.append(j)
    if len(divs) == 3:
        divs.append(i)
        ans.append(divs)

print(*ans, sep='\n')
