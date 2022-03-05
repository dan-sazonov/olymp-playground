# (x + 2y < A) ∨ (y > x) ∨ (x > 30)

a = 1
while True:
    for x in range(1,1000):
        for y in range(1,1000):
            if not ((x + 2*y < a) or (y > x) or (x > 30)):
                break
        else:
            continue
        break
    else:
        print(a)
    a+=1
