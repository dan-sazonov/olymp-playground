a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
ans = 0


def compare(x, y, tmp):
    tmp += min(x, y)
    if x > y:
        return x - y, 0, tmp
    return 0, y - x, tmp


a1, b1, ans = compare(a1, b1, ans)
a2, b2, ans = compare(a2, b2, ans)
a1, b3, ans = compare(a1, b3, ans)
a2, b3, ans = compare(a2, b3, ans)
a3, b1, ans = compare(a3, b1, ans)
a3, b2, ans = compare(a3, b2, ans)
a3, b3, ans = compare(a3, b3, ans)

print(ans)
