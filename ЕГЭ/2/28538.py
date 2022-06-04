# ((x ∧ y) → (¬z ∨ w)) ∧ ((¬w → x) ∨ ¬y).

print('w x y z')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if not (((x and y) <= (not z or w)) and ((not w <= x) or not y)):
                    print(w, x, y, z)
