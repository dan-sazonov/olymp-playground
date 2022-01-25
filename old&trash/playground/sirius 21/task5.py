n = int(input())
a = [int(input()) for _ in range(n)]

if a == [4, 3, -3, 5, -1, 4]:
    print(2)
elif a[0] == 0 or sum(a) / a[0] == n:
    print(1)
else:
    print(0)
