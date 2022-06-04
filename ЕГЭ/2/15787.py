# ((x → y) ∧ (y → w)) ∨ (z ≡ ( x ∨ y)).

print('x w z y')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if not (((x <= y) and (y <= w)) or (z == (x or y))):
                    print(y, w, z, x)
