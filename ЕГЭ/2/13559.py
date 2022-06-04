# ¬ y ∧ (x ∨ ¬ z).

print('x y z')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if not y and (x or not z):
                print(x, y, z)
