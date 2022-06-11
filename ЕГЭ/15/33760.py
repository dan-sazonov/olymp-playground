# ДЕЛ(120, A) ∧ (ДЕЛ(x, 36) → (¬ДЕЛ(x, А) → ¬ДЕЛ(x, 45)))

def f(n, m):
    return n % m == 0


a = 1
while True:
    for x in range(1000):
        if not (f(120, a) and (f(x, 36) <= ((not f(x, a)) <= (not f(x, 45))))):
            break
    else:
        print(a)
    a += 1
