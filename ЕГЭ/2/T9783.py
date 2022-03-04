print('w', 'x', 'y', 'z')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = (x and not y) or (x ==z) or not w
                if not f:
                    print(w, x, y, z)

# w x y z
# 1 0 1 1
