for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = (not (z <= y)) or w or (not x)
                print(w, x, y, z, bool(f))


# 1 1 0 1 True
# 1 1 1 0 1
# 1 0 1 1 1

# 0 1 1 1 False
# 0 1 0 0 False
# 0 1 1 0 False

# zxwy
