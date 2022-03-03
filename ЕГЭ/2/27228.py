print('w x y z')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = ((not x) or y or z) == ((not y) and z and w)
                if f:
                    print(w, x, y, z)
# ywzxf
# 01111
# 00011
# 01011
