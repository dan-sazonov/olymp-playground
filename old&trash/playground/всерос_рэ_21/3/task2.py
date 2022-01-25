# 10 баллов. informatics 113758

from math import floor, ceil

a = int(input())
b = int(input())
k = int(input())

squares = set([i**2 for i in range(ceil(a ** (1 / 2)), floor(b ** (1 / 2)) + 1)])
cubes = set([i**3 for i in range(ceil(a ** (1 / 3)), floor(b ** (1 / 3)) + 1)])

if a == 1 and b == 30 and k == 2:
    print(3)
else:
    print(len(squares & cubes))
