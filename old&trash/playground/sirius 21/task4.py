a = 2 ** int(input())
b = 2 ** int(input())
c = 2 ** int(input())
d = input()

ans = a + b - c

print(str(bin(ans)).count(d))
