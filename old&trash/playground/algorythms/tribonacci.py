n = int(input())
a = 1  # a0
b = 2  # a1
c = 4  # a2
for _ in range(n - 2):
    a, b, c = b, c, a + b + c
print(c)
