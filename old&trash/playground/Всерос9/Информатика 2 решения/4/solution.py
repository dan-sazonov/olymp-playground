N = int(input())
A = int(input())
B = int(input())
C = int(input())

def time(x, y):
    return max(x * C + (N - x) * A, x * C + (x - y - 1) * B, y * A)

ans = N * A
X = (N * A * A + N * A * B) // (2 * A * B + A * A - C * B)
for x in (X, X + 1):
    y = (C + B) * x // (A + B)
    ans = min(ans, time(x, y))
print(ans)

