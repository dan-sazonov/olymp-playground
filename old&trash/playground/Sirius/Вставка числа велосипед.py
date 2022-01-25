n = int(input())
a = list(map(int, input().split()))
number, index = map(int, input().split())

a.append(number)
while True:
    if n >= index:
        a[n-1], a[n] = a[n], a[n-1]
        n -= 1
    else:
        break

print(a)
