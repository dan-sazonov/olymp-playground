# ДЕЛ(90, A) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 15) → ¬ДЕЛ(x, 20)))

def s(n, m):
    return n % m == 0


a = 1
while True:
    for x in range(10000):
        if not (s(90, a) and ((not s(x, a)) <= (s(x, 15) <= (not s(x, 20))))):
            break
    else:

        print(a)
    a += 1
