print('w x y z')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if not (not (x <= z) or (y == w) or not y):
                    print(w, x, y, z)
