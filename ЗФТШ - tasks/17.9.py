a, b = map(int, input().split())

while b > 0:
    tmp = b
    b = a % b
    a = tmp

print(a)
