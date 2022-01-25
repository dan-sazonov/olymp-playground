n = int(input())
painted = []
k = 0
i = 1

for _ in range(n):
    painted.append(list(map(int, input().split())))
painted.sort()

left, right = painted[0]
while i < n:
    a, b = painted[i]
    if b > right:
        if a <= right:
            right = b
        else:
            k += abs(left - right) + 1
            left, right = painted[i]
    i += 1

k += abs(left - right) + 1
print(k)


# painted = []
# k = 0
# i = 1
#
# for _ in range(int(input())):
#     painted.append(list(map(int, input().split())))
# painted.sort()
#
# left, right = painted[0]
# while i < len(painted):
#     a, b = painted[i]
#     if painted[i - 1][1] >= a:
#         left = a if a < left else left
#         right = b if b > right else right
#         i += 1
#     else:
#         k += abs(left - right) + 1
#         left = a
#         right = b
#         i += 1
# k += abs(left - right) + 1
#
# print(k)
