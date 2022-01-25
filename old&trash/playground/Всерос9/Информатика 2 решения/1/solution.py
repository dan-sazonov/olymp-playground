M = int(input())
X = int(input())
Y = int(input())
W = int(input())
H = int(input())
left = X // M
right = (X + W - 1) // M
bottom = Y // M
top = (Y + H - 1) // M
print((right - left + 1) * (top - bottom + 1))

