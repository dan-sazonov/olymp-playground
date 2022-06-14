import itertools

arr = itertools.product('012', repeat=5)

for i in arr:
    s = '2{}1{}2{}1{}2{}1'.format(*i)
    n = int(s, 3)
    if n % 148 == 0:
        print(n, n // 148)
