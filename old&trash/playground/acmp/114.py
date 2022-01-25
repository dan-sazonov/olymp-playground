n, k = map(int, input().split())
d = [0, k - 1]
d0 = [0, 0]

for i in range(1, n):
    d.append( (d[i - 1] + d0[i - 1]) * (k - 1))
    d0.append(d[i-1])
# except IndexError:
#         print(i, d, d0)

print(d, d0)
