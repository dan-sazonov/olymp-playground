# ((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y) ∧ (y → x)).

print('w x y z')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if ((x and w) or (w or z)) == ((z <= y) and (y <= x)):
                    print(w, x, y, z)
