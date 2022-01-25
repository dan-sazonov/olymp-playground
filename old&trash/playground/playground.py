from bisect import *
from math import *
import random
from itertools import permutations
from queue import PriorityQueue


def zero_div_err_esc(x, n):
    return x / n if x and n / x else 'Err'


def lolkek(n):
    ans = int(str(int(str(abs(n))[::-1]))[::-1])
    return ans if n >= 0 else ans * -1


def xor(a, b):
    return a != b


def error(x):
    try:
        print(2 / float(x))
    except ZeroDivisionError:
        print('ZDE')
    except TypeError:
        print('Use correct types!')
    except ValueError:
        print('Incorrect input!')
    else:
        print('Errors not found')
    finally:
        print('You\'ll always see me')

    try:
        assert False
    except AssertionError:
        print('I\'m gone. F')


def f(arr):
    numbers = list(range(arr[0], len(arr) + arr[0]))
    for c in range(len(arr)):
        if numbers[c] != arr[c]:
            return arr[c]
    return None


def file():
    numbers = []
    with open('in.txt', 'r') as f_read:
        for line in f_read:
            numbers.append(int(line.strip()))

    with open('out.txt', 'w') as f_write:
        f_write.write(str(sum(numbers) / len(numbers)))


def lol(string):
    spl = string.split(" ")
    print(spl)
    longest = 0
    i = 0

    while i < len(spl):
        if len(spl[i]) > longest:
            longest = len(spl[i])
        i += 1
    return longest
    # for word in spl:
    #     if len(word) > longest:
    #         longest = len(word)
    #     return longest


greet = lambda: 'hello world!'


def capitalize(s):
    foo = []
    for u_case in range(0, len(s)):
        if u_case % 2 == 0:
            foo.append(s[u_case])
        else:
            foo.append(s[u_case].upper())
    return [''.join(foo), ''.join(foo).swapcase()]


def two_oldest_ages(ages):
    ages.sort()
    return ages[-2::]


def map_learn(foo=[i + 1 for i in range(15)]):
    squares = list(map(lambda x: x ** 2, foo))
    print(squares)

    even = list(filter(lambda x: x % 2 == 0, foo))
    print(even)


def enum(foo=['a', 'b', 'c', 'd', 'e']):
    bar = dict()
    for i in enumerate(foo, 1):
        bar[i[0]] = bar[1]
    print(bar)


def convert(number, base):
    out = []
    while True:
        out.append(str(number % base))
        number //= base
        if number < base:
            out.append(str(number))
            break
    return int(''.join(out))


def triple_trouble(one, two, three):
    bar = []
    for c in list(zip(one, two, three)):
        bar.append(''.join(c))
    return ''.join(bar)


def rec(arr):
    print(arr)
    if not arr:
        return 0
    x = arr[0] + rec(arr[1:])
    print(x)
    print('========')
    return x


# def printer(arr):
#     if not arr:
#         return 0
#     x = arr[0]
#     print(x + '!', '=', factorial.cycle_calc((int(x))))
#     return printer(arr[1:])


def row_sum_odd_numbers(n):
    print(n ** 3)


def in_asc_order(arr):
    print(arr, sorted(arr))
    return bool(arr == sorted(arr))


def my_languages(results):
    foo = list(results.items())
    foo.sort(key=lambda x: x[1])
    return [i[0] for i in reversed(foo) if i[1] >= 60]


def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return pos if pos != hi and a[pos] == x else -1  # don't walk off the end


def r(n):
    return n % 9 or n and 9


def pattern(n):
    return '\n'.join([str(i) * i for i in range(1, n + 1)])


def number(lines):
    return ['%d: %s' % i for i in enumerate(lines, 1)]


def n(data):
    return ['Senior' if i[0] >= 55 and i[1] > 7 else 'Open' for i in data]


def expression_matter(a, b, c):
    return max(a * b * c, a * b + c, (a + b) * c, a + b * c, a * (b + c), a + b + c)


# Test.assert_equals(all_non_consecutive([1,2,3,4,6,7,8,10]), [{'i': 4, 'n': 6}, {'i': 7, 'n': 10}])
def all_non_consecutive(arr):
    res = dict()
    for i in range(1, len(arr)):
        if (arr[i] - arr[i - 1]) != 1:
            res.update('i', i)
    return res


def find_div(n):
    divisor = [1, n]
    for i in range(2, n):
        if n % i == 0:
            divisor.insert(-1, i)
    return divisor


def is_prime(n):
    return len(find_div(n)) > 2


def is_prime_fast(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False


def digits(n):
    total = 0
    mult = 1
    while n > 0:
        total += n % 10
        mult *= n % 10
        n //= 10
    return total, mult


def digits_for(n):
    total, mult = 0, 1
    for i in str(n):
        i = int(i)
        total += i
        mult *= i
    return total, mult


def factorial(n):
    n = abs(n)
    if n <= 1:
        return n or 1
    else:
        return n * factorial(n - 1)


def factorial_cycle(n):
    n = abs(n)
    result = n
    while n > 1:
        result *= n - 1
        n -= 1
    return result or 1


def is_prime_root(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def byte_operations():
    '''
    есть 4 условия. 4, 3, 1 - истинно, 2 - ложно
    '''

    flags = [0b1000, 0b0100, 0b0001]  # создаем три ключа по условию
    flag = 0b0000

    for key in flags:  # запихивыаем в одну переменную
        flag |= key

    if flag & 0b0001:  # проверяем флаги по очереди
        print('Flag #1 is true')
    if flag & 0b0010:
        print('Flag #2 is true')
    if flag & 0b0100:
        print('Flag #3 is true')
    if flag & 0b1000:
        print('Flag #4 is true')

    if not flag:  # если флагов нет
        print('True flags are missing')

    print(bin(flag))


def test_decorator():
    def say_hello(name=''):
        print(f'Wazzup, {name.capitalize()}')

    def attention():
        print('Attention please!')

    def respect_attention(name=''):
        print(f'Thanks for your attention, {name.capitalize()}!')

    def some_wrapper(func, arg):
        print('\n=====Pretty top border=====')
        func(arg)
        print('====Pretty lower border====\n')

    def wrapper(name):
        some_wrapper(say_hello, name)
        attention()
        some_wrapper(respect_attention, name)


def decorator():
    def another_decorator(func):
        def wrapper(who):
            print('before function')
            func(who)
            print('after function')

        return wrapper

    n = 3
    name = 'Dan'

    @another_decorator
    def say_whee(give):
        print('Hi ' + give)

    # say_whee = another_decorator(say_whee, n, name)
    # say_whee('the end')

    say_whee(name)


def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


def say_name(num):
    def full_name():
        return 'Daniel'

    def short_name():
        return 'Dan'

    def no_name():
        return 'man'

    if num == 1:
        return full_name
    elif num == 2:
        return short_name
    else:
        return no_name


def say_compliment(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('You\'re a good man!\n')
        # return func(*args, **kwargs)

    return wrapper


# @say_compliment
# def greeting(variant):
#     user_name = say_name(variant)
#     print(f'Hi, {user_name()}!')
#
#
# @do_twice
# def return_greeting(name):
#     print("I'm here!")
#     return f'Hello {name}'
#
#
# # return_greeting('Dan')
# print(return_greeting('Dan'))
# !/usr/bin/env python3

def diof():
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def aer(a, b):
        x2 = 1
        x1 = 0
        y2 = 0
        y1 = 1
        while b != 0:
            q = a // b
            r = a - q * b
            x = x2 - q * x1
            y = y2 - q * y1
            a, b = b, r
            x2, x1 = x1, x
            y2, y1 = y1, y
        return x2

    a = int(input())
    b = int(input())
    c = int(input())

    if a < b:
        a, b = b, a
    x = aer(a, b)
    y = int((gcd(a, b) - a * aer(a, b)) / b)

    if c % gcd(a, b) == 0:
        print('x=' + str(int(x * c / gcd(a, b))) + '+' + str(int(b / gcd(a, b))) + 't;y=' + str(
            int(y * c / gcd(a, b))) + str(int(-a / gcd(a, b))) + 't')
    else:
        print('Решений нет')


def fucktorization(n):
    p = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            p.append(d)
            n //= d
        d += 1
    if n > 1:
        p.append(n)
    return p


def phi_test(n):
    res = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            res -= res // p
        while n % p == 0:
            n //= p
        p += 1
    if n > 1:
        res -= res // n
    return res


def phi_correct(n):
    result = n
    i = 1

    while n + 1 > i ** 2:
        i += 1
        if not n % i:
            while not n % i:
                n //= i
            result -= result // i
            continue

    return result if n <= 1 else result - (result // n)


def phi_tester():
    err_log = []
    err_counter = 0
    for j in range(100):
        n = random.randint(1, 10000000)
        if phi_test(n) != phi_correct(n):
            err_log.append(n)
            err_counter += 1

    print(err_log, err_counter, sep='\n')


def lower_bound(a, x):
    n = len(a)
    L = -1
    R = n
    while R - L > 1:
        M = (R + L) // 2
        if a[M] < x:
            L = M
        else:
            R = M
    if R < n and a[R] == x:
        print(R)
    else:
        print(-1)
    print(bisect_left(a, x))


def upper_bound(a, x):
    n = len(a)
    L = -1
    R = n
    while R - L > 1:
        M = (R + L) // 2
        if a[M] <= x:
            L = M
        else:
            R = M
    if L < n and a[L] == x:
        print(R)
    else:
        print(-1)
    print(bisect_right(a, x))


def bisect_test():
    a = [1, 2, 3, 4, 4, 4, 5, 6, 9]
    x = 1
    lower_bound(a, x)
    upper_bound(a, x)


def root_bisect(a, n):
    L = 0
    R = a
    for i in range(200):
        M = (R + L) / 2
        if M ** n < a:
            L = M
        else:
            R = M
    return R


def test_root_bisect(accuracy=4):
    err_counter = 0
    err_log = []
    for _ in range(1000):
        a = random.randint(1, 1000)
        n = random.randint(1, 10)
        if round(root_bisect(a, n), accuracy) != round((a ** (1 / n)), accuracy):
            err_counter += 1
            err_log.append([a, n])

    # print(err_counter)
    # print(err_log)
    return err_counter


def test_accuracy_root_bisect():
    err_counter = set()
    for _ in range(100):
        err_counter.add(test_root_bisect(11))
    print('ok' if len(err_counter) == 1 else 'err')


def fuck(a, n):
    inf = int(2e9) + 1
    a = [-inf] + a + [-inf]
    ans = [0] * (n + 2)
    st = [0]
    for i in range(1, n + 2):
        while a[st[-1]] > a[i]:
            ans[st.pop()] = i
        st.append(i)
    print(ans[1:-1])


def prime():
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


def transpose():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    a_t = list(zip(*a))
    print(a_t)


def test_version():
    import sys

    print('lol')
    print(sys.version_info)


def files():
    with open('in.txt') as r:
        a, b = map(int, r.read().split())
    with open('out.txt', 'w') as w:
        w.write(str(a + b))


files()
for i in range(1, len(str(n))):
    if str(n)[i] == str(n)[i - 1]:
        print('не подходит')
