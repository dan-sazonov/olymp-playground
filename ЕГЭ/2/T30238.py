print('w', 'x', 'y', 'z')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = ((y == w) or (z <= w)) and (y == (x or z))
                if f:
                    print(w, x, y, z)


# 0 1 1 0