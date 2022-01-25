n = int(input())
ans = [0, 0, 0, 0]


def one_sq(n):
    left, right = 0, n
    while right > left + 1:
        middle = (left + right) // 2
        if middle * middle >= n:
            right = middle
        else:
            left = middle
    if right * right == n:
        return right
    return False


def two_sq(n):
    a = 1
    while a * a < n:
        x = one_sq(n - a * a)
        if x:
            return list(sorted((a, x)))
        a += 1
    return False


def three_sq(n):
    a = 1
    while a * a < n:
        x = two_sq(n - a * a)
        if x:
            return list(sorted((x[0], x[1], a)))
        a += 1
    return False


def four_sq(n):
    a = 1
    while a * a < n:
        x = three_sq(n - a * a)
        if x:
            return list(sorted((x[0], x[1], x[2], a)))
        a += 1
    return False


if n % 4 == 3:
    x3 = three_sq(n)
    if x3:
        ans = [x3[0], x3[1], x3[2]]
    else:
        x4 = four_sq(n)
        ans = [x4[0], x4[1], x4[2], x4[3]]
elif n % 4 == 2:
    x2 = two_sq(n)
    if x2:
        ans = [x2[0], x2[1]]
    else:
        x3 = three_sq(n)
        if x3:
            ans = [x3[0], x3[1], x3[2]]
        else:
            x4 = four_sq(n)
            ans = [x4[0], x4[1], x4[2], x4[3]]
else:
    x1 = one_sq(n)
    if x1:
        ans = [x1]
    else:
        x2 = two_sq(n)
        if x2:
            ans = [x2[0], x2[1]]
        else:
            x3 = three_sq(n)
            if x3:
                ans = [x3[0], x3[1], x3[2]]
            else:
                x4 = four_sq(n)
                ans = [x4[0], x4[1], x4[2], x4[3]]

print(*ans)
