# (x ∨ y) ∧ ¬(y ≡ z) ∧ ¬w

print('w x y z')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if (x or y) and not (y == z) and not w:
                    print(z, y, x, w)

# 1		1		1
# 0	1		0	1
# 	1	1	0	1
