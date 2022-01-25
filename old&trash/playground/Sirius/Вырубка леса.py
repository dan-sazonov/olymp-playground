# a, k, b, m, x = map(int, input().split())
# days = 0
#
# while x > 0:
#     if (days + 1) % b != 0:
#         x -= a
#     if (days + 1) % m != 0:
#         x -= k
#     days += 1
#
# days += x if x >= 0 else 0
# print(days)

# a, k, b, m, x = map(int, input().split())
# days = 0
#
# while x > 0:
#     if (days + 1) % b != 0:
#         x -= a
#     if (days + 1) % m != 0:
#         x -= k
#     days += 1
#
# days += 1 if x >= 0 else 0
# print(days)


a, k, b, m, x = map(int, input().split())
days = 0

while x > 0:
    if (days + 1) % b != 0:
        x -= a
    if (days + 1) % m != 0:
        x -= k
    days += 1

print(days)
