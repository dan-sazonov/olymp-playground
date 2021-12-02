a, b = 0, 1
n = int(input())

while n:
    n -= 1
    a, b = b, a+b

print(b)
