# (¬x ∧ y ∧ z) ∨ (¬x ∧ ¬y ∧ z) ∨ (¬x ∧ ¬y ∧ ¬z).

print('x', 'y', 'z')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if (not x and y and z) or (not x and not y and z) or (not x and not y and not z):
                print(x, y, z)

# x y z
# 0 0 0
# 0 0 1
# 0 1 1
