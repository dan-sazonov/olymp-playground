a, b, c, d = map(int, input().split())
right = 2000
eps = 1e-12


def find_root(x):
    return a*x*x*x + b*x*x + c*x + d


left = -right

while right - left > eps:
    m = (right + left) / 2
    if find_root(m) * find_root(right) > 0:
        right = m
    else:
        left = m


print(right if a > 0 else left)
