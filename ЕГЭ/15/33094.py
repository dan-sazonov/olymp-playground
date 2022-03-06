# (A < 50) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 10) → ¬ДЕЛ(x, 18)))


def f(n, m):
    return n % m == 0


a = 1
while True:
    for x in range(1, 90_000):
        if not ((a < 50) and ((not f(x, a)) <= (f(x, 10) <= (not f(x, 18))))):
            break
    else:
        print(a)
    a += 1
