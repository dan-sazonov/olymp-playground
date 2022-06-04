# ((x ∧ ¬y) ∨ (w → z)) ≡ (z ≡ x).

print('w z x y')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if ((x and not y) and (w <= z)) == (z == x):
                    print(w, z, x, y)
