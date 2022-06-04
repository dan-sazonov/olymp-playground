# ¬w ∧ z ∧ (y → x).

print('w x y z')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if not w and z and (y <= x):
                    print(w, x, y, z)
