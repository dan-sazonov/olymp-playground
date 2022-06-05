# (¬x ∨ ¬y) ∧ ¬(x ≡ z) ∧ w.

print('w x y z')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if (not x or not y) and not (x == z) and w:
                    print(w, x, y, z)
