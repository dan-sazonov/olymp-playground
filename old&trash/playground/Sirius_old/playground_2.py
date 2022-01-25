def last_number():
    number = int(input())
    ans = 1
    for c in range(1, number + 1):
        ans *= c
    print(str(ans).rstrip('0')[-1])


def find_house_place():
    a, b, d = map(int, input().split())
    school_to_club = abs(a - b)
    dist_1, dist_2 = -1, 2

    if school_to_club > 1:
        dist_1 = school_to_club // 2
        dist_2 = school_to_club - dist_1

    point_1, point_2 = min(a, b) + dist_1, min(a, b) + dist_2
    tmp_1, tmp_2 = point_1 % d, point_2 % d

    dist_to_ice_1 = min(tmp_1, d - tmp_1)
    dist_to_ice_2 = min(tmp_2, d - tmp_2)

    if dist_to_ice_1 <= dist_to_ice_2:
        print(point_1, dist_to_ice_1)
    else:
        print(point_2, dist_to_ice_2)


def vasya():
    from math import floor, ceil
    a, b, d = map(int, input().split())
    house = distance1 = distance2 = n = 0
    middle = (b - a) / 2 + a

    if (b - a) % 2 == 0:
        house = int(middle)
    else:
        if floor(middle) % 4:
            house = floor(middle)
            distance1 = 0
        else:
            n = floor(middle)
            while n % 4 != 0:
                n -= 1
                # ищем ближайшее кратное n 4 меньше floor(middle)
            distance1 = floor(middle) - n
            house = n
            pass
        if ceil(middle) % 4:
            house = ceil(middle)
            distance2 = 0
        else:
            n = ceil(middle)
            while n % 4 != 0:
                n += 1
                # ищем ближайшее кратное n 4 больше ceil(middle)
            distance2 = n - ceil(middle)
            house = n
            pass

    print(house, min(distance1, distance2))


def inverse_number():
    numbers = [[int(i) for i in input().split()] for _ in range(int(input()))]
    for pair in numbers:
        x, y, z = pair[1], pair[0] - 2, pair[0]
        res = 1
        p = x % z
        while y:
            if y & 1:
                res = (res * p) % z
            y >>= 1
            p = (p * p) % z
        print(res)


def lcd():
    from math import gcd
    a, b = map(int, input().split())
    print((a * b) // gcd(a, b))


def simp():
    from math import gcd
    a, b = map(int, input().split())
    divisor = gcd(a, b)
    print(a // divisor, b // divisor)


def line():
    from math import gcd
    a, b, c, d = map(int, input().split())
    x, y = abs(a - c), abs(b - d)
    common = gcd(x, y)
    print(common * (x // common + y // common - 1))


def last_number_fast():
    n = int(input())
    counter, number = 0, 1
    for i in range(1, n + 1):
        x = i
        while x % 2 == 0:
            x //= 2
            counter += 1
        while x % 5 == 0:
            x //= 5
            counter -= 1
        number = number * x % 10
    for i in range(counter):
        number = number * 2 % 10
    print(number)


def diophantine():
    def nod(m, n):
        return m if n == 0 else nod(n, m % n)

    a = int(input("A = "))
    b = int(input("B = "))
    c = int(input("C = "))

    assert c != 0

    nodAB = nod(abs(a), abs(b))
    if c % nodAB:
        print("Impossible")
    else:
        a //= nodAB
        b //= nodAB
        c //= nodAB

        for k in range(abs(a)):
            if (c - b * k) % a == 0:
                y = k
                x = (c - b * y) // a
                print("X =", x, "Y =", y)
                break
        else:
            print("Shit happens!")


def power(number):
    from functools import reduce

    def factorize(n):
        i = 2
        primes = []
        while i * i <= n:
            while not n % i:
                primes += [i]
                n /= i
            i += 1
        if n > 1:
            primes += [n]
        return list(set(primes))

    # number = int(input())
    factors = factorize(number) + [1]
    prod = reduce((lambda a, b: a * b), factors)

    if factors[0] != number:
        for j in range(40):
            tmp = (j + 1) * prod
            if not (pow(tmp, tmp) % number):
                print(tmp)
                break
    else:
        print(int(factors[0]))


def power_true():
    from sys import setrecursionlimit
    setrecursionlimit(10 ** 9)  # увеличение максимальной глубины рекурсии

    def fast_pow(a, n):  # функция быстрого возведения в степень
        if n == 0:
            return 1
        elif n == 1:
            return a
        elif n % 2 != 0:
            return a * fast_pow(a, n - 1)
        elif n % 2 == 0:
            return fast_pow(a * a, n / 2)

    def decomp(n):  # функция разложения числа на простые множители
        ans = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            ans.append(n)
        return ans

    x = int(input())
    a = list(set(decomp(x)))  # разложение числа x на простые множители в единственном экземпляре
    b = decomp(x)  # разложение числа x на простые множители

    y = 1
    for i in range(len(a)):  # перемножение простых множителей
        y *= a[i]
    k = 1
    n = k * y

    if a[0] != x:
        for i in range(40):
            if fast_pow(((i + 1) * y), ((i + 1) * y)) % x == 0:
                print((i + 1) * y)
                break
    else:
        print(a[0])


def is_prime_sirius():
    from math import sqrt

    def is_prime(n):
        for i in range(2, int(sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True

    print('YES' if is_prime(int(input())) else 'NO')


# def find_div(n=int(input())):
#     i = 2
#     while n >= i ** 2:
#         if not n % i:
#             return i
#         i += 1
#     return n


def num_func():
    from math import sqrt

    n = int(input())
    ans, sigma_0 = 0, 2

    for i in range(2, int(sqrt(n)) + 1):
        if not n % i:
            sigma_0 += 2
            ans = ans + i + n // i
    sigma_1 = n + ans + 1

    print(sigma_0, sigma_1)


def num_func_2():
    from math import sqrt

    n = int(input())
    sigma_0 = sigma_1 = 0

    for i in range(1, int(sqrt(n)) + 1):
        if not n % i and i != sqrt(n):
            sigma_0 += 2
            sigma_1 += i + n // i
        elif not n % i and i == sqrt(n):
            sigma_0 += 1
            sigma_1 += i

    print(sigma_0, sigma_1)


def eratosthenes():
    from math import sqrt

    def is_prime(n):
        for i in range(2, int(sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True

    k = int(input())
    number = 2
    j = 0
    while True:
        if is_prime(number):
            j += 1
            if j == k:
                break
        number += 1
    print(number)


def euler():
    import math
    res = []
    for i in range(1, 239):
        if math.gcd(239, i) == 1:
            res.append(i)
    if len(res) == 0:
        print('2')
    elif len(res) == 238:
        print('1')
    else:
        print('3')


def phi():
    n = int(input())
    result = n
    i = 1

    while n + 1 > i ** 2:
        i += 1
        if not n % i:
            while not n % i:
                n //= i
            result -= result // i
            continue

    print(result if n <= 1 else result - (result // n))


def inverse():
    def gcd(a, b):
        if not a:
            return b, 0, 1
        div, x1, y1 = gcd(b % a, a)
        y = y1 - (b // a) * x1
        return div, y, x1

    m, a = map(int, input().split())
    gcd, x, _ = gcd(a, m)
    number = (x % m + m) % m
    print(number if gcd == 1 else -1)


def divisors():
    from math import gcd

    n = int(input())
    pairs = []
    i = amount = 0

    while i ** 2 <= n:
        i += 1
        mod, div = n % i, n // i
        if not mod:
            pairs.extend([i, div])
    pairs = sorted(list(set(pairs)))

    for i in range(len(pairs) - 1):
        for j in range(i + 1, len(pairs)):
            if n < pairs[i] * pairs[j]:
                break
            elif gcd(pairs[i], pairs[j]) == 1:
                amount += 1

    print(amount)


def fun_game():
    from math import gcd

    n = int(input())
    a = list(map(int, input().split()))
    amount = 0

    for i in range(n):
        if amount > n - i:
            break
        item = a[i]
        ans = 0

        for j in range(i, n):
            ans += 1
            item = gcd(a[j], item)
            if item == 1:
                break
            a[j] //= item
            amount = ans if ans > amount else amount

    print(amount)


def even_spaced():
    from math import sqrt

    def count():
        n = int(input())
        d = 0
        out = ['single']

        while not (n & 1):
            d += 1
            n //= 2

        a = [2] * d
        a[-1] *= n

        if d == 1:
            return 'prime'

        for i in range(3, int(sqrt(n)) + 1, 2):
            if not (n % i):
                b = a[:]
                b[-1] //= i
                b[-2] *= i
                out.append(' '.join(map(str, a)))
                out.append(' '.join(map(str, b)))
            return None

        out.append(' '.join(map(str, a)))
        return '\n'.join(out)

    print(count())


def fucktorials():
    def factorize(n):
        ans = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            ans.append(n)
        return ans

    x = int(input())
    if x == 1:
        print(1)
    else:
        a = list(set(factorize(x)))
        b = factorize(x)
        y = 1
        for i in range(len(a)):
            y *= a[i]
        k = 1
        n = k * y
        if a[0] != x:
            for i in range(40):
                t = (i + 1) * y
                if pow(t, t, x) == 0:
                    print((i + 1) * y)
                    break
        else:
            print(a[0])


def factor_divs():
    from math import factorial, sqrt

    def factor(n):
        res = []
        i = 2
        while i <= sqrt(n):
            if n % i == 0:
                res.append(i)
                n //= i
            else:
                i += 1
        if n > 1:
            res.append(n)
        return res

    n = int(input())
    if n == 1:
        print(1)
    else:
        primes = factor(factorial(n))
        ans, num, current, = 1, 1, primes[0]
        for j in range(1, len(primes)):
            if primes[j] == current:
                num += 1
            else:
                ans *= num + 1
                num = 1
                current = primes[j]
        print(ans * (num + 1))


def j_true():
    from math import factorial

    def factor(n):
        res = []
        i = 2
        while i * i <= n:  # Ищем только до корня из n
            if n % i == 0:
                res.append(i)
                n //= i
            else:
                i += 1
        if n > 1:
            res.append(n)
        return res

    n = int(input())
    if n == 1:  # Факторизация единицы ничего не даст, обработаем её отдельно
        print(1)
    else:
        primes = factor(factorial(n))  # Рассчитываем факториал и получаем все простые делители
        # Наш ответ будем умножать в процессе, поэтому 1
        # num отвечает за количество повторений актуального простого делителя
        # последний обработанный простой делитель, начинаем с первого элемента
        answer, num, actual, length = 1, 1, primes[0], len(primes)
        for i in range(1, length):  # Начинаем с 1, тк 0 элемент мы уже обработали
            if primes[i] == actual:  # Если такой уже был, то просто увеличиваем счетчик
                num += 1
            else:  # Если это новый простой делитель
                answer *= num + 1  # домножаем ответ на инкрементированное кол-во одинаковых делителей
                num = 1  # Обработка происходит уже на новом элементе, учитываем его
                actual = primes[i]  # Меняем текущий элемент
        answer *= num + 1  # Последняя обработка не попадет в цикл, домножим так
        print(answer)


def kl():
    from math import sqrt

    def solve(n):
        j = 0
        while not (n & 1):
            j += 1
            n //= 2

        a = [2] * j
        a[-1] *= n

        if j == 1:
            print('prime')
            return None

        for i in range(3, int(sqrt(n)) + 1, 2):
            if not (n % i):
                b = a[:]
                b[-1] //= i
                b[-2] *= i
                print('many')
                print(' '.join(map(str, a)))
                print(' '.join(map(str, b)))
                return None

        print('single')
        print(' '.join(map(str, a)))

    solve(int(input()))


def ff():
    a, b = map(int, input().split())

    numbers = [0, 0] + list(range(2, b + 1))
    primes = []

    i = 2
    while i <= b:
        if numbers[i] != 0:
            primes.append(numbers[i])
            for j in range(i, b + 1, i):
                numbers[j] = 0
        i += 1

    super_numbers = []
    for j in range(len(primes)):
        for c in range(len(primes) - 1):
            g = primes[j] + primes[c]
            if a <= g <= b:
                super_numbers.append(g)

    print(*sorted(list(set(super_numbers))), sep='\n')


def sa():
    n = int(input())
    basis = 2
    res = []
    do_power = False
    while n != 1:
        while n % basis != 0:
            basis += 1
        exp = 0
        while n % basis == 0:
            n //= basis
            exp += 1
        if do_power:
            res.append('*')
        else:
            do_power = True
        if exp > 1:
            res.append('%d^%d' % (basis, exp))
        else:
            res.append(str(basis))
        basis += 1
    print(''.join(res))


def bd():
    '''
    var n,a,b,c:integer;
    begin
    write('n=');
    readln(n);
    a:=2;
    while a<=n do
     begin
      b:=0;
      while n mod a=0 do
       begin
        inc(b);
        n:=n div a;
       end;
      if b=1 then write(a)
      else if b>1 then write(a,'^',b);
      inc(a);
      if (b>0)and(a<n) then write('*');
     end;
     end.
    '''
    pass


def ld():
    def is_prime(n):
        for i in range(2, int((n ** .5) + 1)):
            if n % i == 0:
                return False
        return True

    k = int(input())
    n = 2
    while k > 0:
        k -= 1 if is_prime(n) else 0
        n += 1
    print(n - 1)



def st():
    n = int(input())
    d = 2
    cnt = 0
    res = []
    while n > 1:
        if n % d == 0:
            cnt += 1
            n //= d
        if n % d != 0:
            if cnt == 0:
                pass
            elif cnt == 1:
                res.append(f'{d}*')
            else:
                res.append(f'{d}^{cnt}*')
            d += 1
            cnt = 0
    print(''.join(res).rstrip('*'))


def last_stand():
    n = int(input())
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, n + 1):
        if not prime[i]:
            continue
        for j in range(i * i, n + 1, i):
            prime[j] = False
    print(prime)


def ff():
    n = int(input())
    basis = 2
    do_power = False
    while n != 1:
        while n % basis != 0:
            basis += 1
        exp = 0
        while n % basis == 0:
            n //= basis
            exp += 1
        if do_power:
            print('*', end='')
        else:
            do_power = True
        if exp > 1:
            print(str(basis) + '^' + str(exp), end='')
        else:
            print(basis, end='')
        basis += 1