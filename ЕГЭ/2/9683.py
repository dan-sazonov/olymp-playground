# (¬z)∧x

print('x z f')

for x in 0, 1:
    for z in 0, 1:
        print(x, z, int((not z) and x))

# y x   z
# 0	0	0	0
# 0	0	1	0
# 0	1	1	0
# 1	0	0	0
# 1	0	1	0
# 1	1	1	0

# 1	1	0	1
# 0	1	0	1
