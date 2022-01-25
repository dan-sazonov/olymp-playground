# n = int(input())
# a = int(input())
# b = int(input())
# c = int(input())
# ans = n * a
#
#
# def max_time(x_i, y_i):
#     return max(x_i * c + (n - x_i) * a, x_i * c + (x_i - y_i - 1) * b, y_i * a)
#
#
# for i in range(1, n + 1):
#     for j in range(i + 1):
#         ans = max_time(i, j) if max_time(i, j) < ans else ans
# print(ans)

n = int(input())
a = int(input())
b = int(input())
c = int(input())
ans = n * a


def max_time(x_i, y_j):
    return max(x_i * c + (n - x_i) * a, x_i * c + (x_i - y_j - 1) * b, y_j * a)


x_0 = ((n * a ** 2) + n * a * b) // (2 * a * b + a * a - c * b)
for i in (x_0, x_0 + 1):
    j = (c + b) * i // (a + b)
    ans = min(ans, max_time(i, j))
print(ans)
