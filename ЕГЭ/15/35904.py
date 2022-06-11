# ДЕЛ(A, 40) ∧ (ДЕЛ(780, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(180, x)))

def f(n, m):
    return n % m == 0


a = 1
while True:
    for x in range(1, 1000):
        if not (f(a, 40) and (f(780, x) <= ((not f(a, x)) <= (not f(180, x))))):
            break
    else:
        print(a)
        break
    a += 1
