n = int(input())
a = 2
b = 4
for _ in range(n - 2):
    a, b = b, a + b

print(b)
