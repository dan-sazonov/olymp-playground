x1, y1, x2, y2 = map(int, input().split())
x3, y3, r = map(int, input().split())
#
# if not (x3 in range(min(x1, x2), max(x1, x2) + 1) and y3 in range(min(y1, y2), max(y1, y2) + 1)):
#     print('')
#     exit()

w, w1 = min(abs(y2 - y3), r - 1), min(abs(y1 - y3), r - 1)
h, h1 = min(abs(x2 - x3), r - 1), min(abs(x1 - x3), r - 1)

corr = sum((abs(y2 - y3) >= r, abs(x3 - x1) >= r, abs(y1 - y3) >= r, abs(x2 - x3) >= r))

w_ = w + w1 + 1
h_ = h + h1 + 1
print((w_ * h_) + corr)
# print(w, w1, h, h1, corr)
