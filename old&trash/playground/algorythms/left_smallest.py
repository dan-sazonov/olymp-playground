inf = int(2e9) + 1
# n = int(input())
# a = [-inf] + [int(x) for x in input().split()] + [-inf]
n = 6
a = [3, 6, 8, 4, 2, 5]
#
ans = []
swap = False

for i in range(len(a)):
    i_min = 0
    for j in range(0, i + 1):
        if a[j] < a[i_min]:
            if a[j] < a[i]:
                i_min = j
                swap = True
    ans.append(i_min if swap else -1)

for k in ans:
    print(a[k] if k != -1 else -1)
