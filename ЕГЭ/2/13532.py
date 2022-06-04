# ¬ z ∧ (¬ x ∨ y).

print('x y z')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if not z and (not x or y):
                print(x, y, z)
