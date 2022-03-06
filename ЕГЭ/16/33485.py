# ДЕЛ(120, A) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 18) → ¬ДЕЛ(x, 24)))


def f(n, m):
    return n % m == 0


a = 1
while True:
    for x in range(1, 120*18*24+1):
        if not (f(120, a) and ((not f(x,a)) <= (f(x,18) <= (not f(x, 24))))):
            break
    else:
        print(a)
    a += 1
