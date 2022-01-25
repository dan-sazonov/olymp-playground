# def find_perms(x, y, z, second=False):
#     ans = [max(x, y, z),
#            x + max(y, z),
#            y + max(x, z),
#            z + max(x, y),
#            max(x, y + z),
#            max(y, x + z),
#            max(z, x + y),
#            x + y + z]
#     return ans
#

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())

min_area = 10e4 + 1

# for i in find_perms(a1, a2, a3):
#     for j in find_perms(b1, b2, b3, True):
#         if i * j < min_area:
#             print(i * j, i, j, min_area)
#             min_area = i * j
#         # min_area = min(min_area, i * j)

print((a1 + a2 + a3) * max(b1, b2, b3))
print((a1 + max(a2, a3)) * max(b1, b2 + b3))

# print(min_area)
