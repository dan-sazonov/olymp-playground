x = int(input())
y = int(input())
n = int(input())
a = x + y
prod = n // a * 2

print(prod if (not n % a) else (prod + 2) if (n % a > y) else (prod + 1))
