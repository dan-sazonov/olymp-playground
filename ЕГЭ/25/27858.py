def find_divs(n):
    divs = 1
    for i in range(1, n // 2 + 2):
        if n % i == 0:
            divs += 1
    return divs


divs_max = 0
i_max = 0

for i in range(120115, 120201):
    divs = find_divs(i)
    if divs >= divs_max:
        divs_max = divs
        i_max = i

print(divs_max, i_max)
