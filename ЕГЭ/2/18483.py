print('w x y z')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = ((y <= w) == (x <= (not z))) and (x or w)
                print(w, x, y, z, f)

# yzwxf
# 01110
# 10101
# 00011

# 1 1 0 1 False

# 1 0 0 1 1
# 1 0 1 0 1
# 1 1 0 0 1

# 0 1 0 0 1
