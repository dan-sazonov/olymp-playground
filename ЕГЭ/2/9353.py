# (¬z)∧x ∨ x∧y

print('z y x f')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            print(z, y, x, ((not z) and x or x and y))

# 0 0 0 0
# 1 0 0 1

