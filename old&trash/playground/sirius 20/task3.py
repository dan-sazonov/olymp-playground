width = int(input())
n = int(input())
plates = [int(input()) for i in range(n)]
amount, max_width = 0, 0

for j in plates:
    if j and not max_width:
        amount += 1
        max_width = width
    max_width -= 1 if max_width > 0 else 0

print(amount)

"""
3
8
0
0
1
0
1
0
1
0
"""
