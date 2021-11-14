x1, y1, x2, y2 = map(int, input().split())

w_targets = {
    x1 - 2: {y1 + 1, y1 - 1},
    x1 - 1: {y1 - 2, y1 + 2},
    x1 + 1: {y1 - 2, y1 + 2},
    x1 + 2: {y1 - 1, y1 + 1}
}


def find_diag(x_s, y_s, x_f, y_f):
    x = x_s
    y = y_s
    if x2 > x_s and y2 > y_s:
        while x <= x2 or y <= y2:
            y += 1
            x += 1
            if x == x2 and y == y2:
                return True
    if x2 > x_s and y2 < y_s:
        while x <= x2 or y >= y2:
            y -= 1
            x += 1
            if x == x2 and y == y2:
                return True
    if x2 < x_s and y2 > y_s:
        while x >= x2 or y <= y2:
            y += 1
            x -= 1
            if x == x2 and y == y2:
                return True
    if x2 < x_s and y2 < y_s:
        while x >= x2 or y >= y2:
            y -= 1
            x -= 1
            if x == x2 and y == y2:
                return True


if x1 % 2 == 0:
    fig = 'b' if y1 % 2 == 0 else 'w'
else:
    fig = 'w' if y1 % 2 == 0 else 'b'

if fig == 'w':
    for i in w_targets:
        if x2 == i and y2 in w_targets[i]:
            print(1, f'{x2} {y2}', sep='\n')
            exit()
else:
    if find_diag(x1, y1, x2, y2):
        print(1, f'{x2} {y2}', sep='\n')
        exit()

print(-1)
