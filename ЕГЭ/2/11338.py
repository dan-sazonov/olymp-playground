# x ∧ ¬y ∧ (¬z ∨ w).

print('w x y z')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if x and not y and (not z or w):
                    print(w, x, y, z)
