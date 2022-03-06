# ДЕЛ(A, 45) ∧ (ДЕЛ(750, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(120, x)))


def f(n, m):
    return n % m == 0


a = 1
while True:
    for x in range(1, 1_000_000):
        if not(f(a, 45) and (f(750, x))) <= ((not f(a, x)) <= (not f(120, x))):
            break
    else:
        print(f'=========={a}')
    print(a)
    a += 1