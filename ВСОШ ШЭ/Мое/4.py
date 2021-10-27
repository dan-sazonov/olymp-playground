n = int(input())
d = int(input())
a = [int(input()) for _ in range(n)]
a_max = a[0] // d + 1

for i in range(1, len(a)):
    if i + 1 <= a_max:
        tmp = a[i] // d + i + 1
        if a_max < tmp:
            a_max = tmp
    else:
        break

print(len(a) if a_max > len(a) else a_max)
