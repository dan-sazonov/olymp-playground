def alt_merge_sort():
    n = int(input())
    arr = list(map(int, input().split()))

    def merge(left, right):
        res = []
        count = 0
        l_index, r_index = 0, 0

        while count < len(left) + len(right):
            if l_index < len(left) and r_index < len(right):
                if left[l_index] <= right[r_index]:
                    res.append(left[l_index])
                    l_index += 1
                else:
                    res.append(right[r_index])
                    r_index += 1

            elif l_index == len(left):
                res.append(right[r_index])
                r_index += 1
            elif r_index == len(right):
                res.append(left[l_index])
                l_index += 1
            count += 1
        return res

    def m_s(nums):
        half = len(nums) // 2
        if len(nums) > 1:
            return merge(m_s(nums[:half]), m_s(nums[half:]))
        return nums

    print(' '.join(map(str, m_s(arr))))


def unusable_sort():
    n, k = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))

    for i in range(n - 1):
        pivot = i
        for j in range(i + 1, n):
            if arr[j] < arr[pivot]:
                pivot = j
        arr[i], arr[pivot] = arr[pivot], arr[i]

    print(arr[-k])


def selection_sort():
    import queue
    q = queue.PriorityQueue()
    n, k = map(int, input().split())
    for x in input().split():
        q.put(int(x))
        if q.qsize() > k:
            q.get()
    print(q.get())


def slow_bubble_sort(arr):
    n = len(arr)
    iter_counter, while_counter, for_counter = 0, 0, 0
    unordered = True
    while unordered:
        while_counter += 1 if unordered else 0
        print(arr)
        unordered = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                unordered = True
                for_counter += 1
        iter_counter += 1 if unordered else 0
        n -= 1
    return arr, iter_counter, while_counter, for_counter


str_to_list = lambda line: list(map(int, line.split()))


def bubble_sort_counter():
    n = int(input())
    arr = list(map(int, input().split()))
    unordered = True
    iter_counter = 0
    while unordered:
        unordered = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                unordered = True
                iter_counter += 1
        n -= 1
    print(iter_counter)


def gen():
    n, k = tuple(map(int, input().split()))
    unordered = True
    num = list(range(1, n + 1))
    iter_counter = 0

    while unordered and iter_counter < k:
        unordered = False
        for i in range(n - 1):
            if num[i] < num[i + 1] and iter_counter < k:
                num[i + 1], num[i] = num[i], num[i + 1]
                iter_counter += 1
                unordered = True

    print(' '.join(map(str, num)))


def sirius_first(a, n):
    # a = int(input())
    # n = int(input())
    res = 0

    if n > 0 > a and a + n > 0:
        res = a + n + 1
    elif a > 0 > n and a + n < 0:
        res = a + n - 1
    elif n > 0 > a and a + n == 0:
        res = 1
    elif a > 0 > n and a + n == 0:
        res = -1
    else:
        res = a + n

    # print(res)
    return res


def another_sirius_first(a, n):
    # a = int(input())
    # n = int(input())
    res = 0

    if abs(a) <= abs(n) and ((a > 0 and n < 0) or (a < 0 and n > 0)):
        if n > 0:
            res = a + n + 1
        elif n < 0:
            res = a + n - 1
    else:
        res = a + n

    # print(res)
    return res


def sirius_man_test_1(a, n):
    # a = int(input())
    # n = int(input())
    f1 = sirius_first(a, n)
    f2 = another_sirius_first(a, n)
    print('True: {0}|{1}'.format(f1, f2) if f1 == f2 else 'False: {0}|{1}'.format(f1, f2))
    return f1, f2


def sirius_auto_test_1():
    err = []
    for i in range(-10 ** 9, 10 ** 3):
        for j in range(-10 ** 3, 10 ** 3):
            res = sirius_man_test_1(i, j)
            if res[0] != res[1]:
                err.append('{0}{1}'.format(i, j))
                print('{0}{1}'.format(i, j))
    return '\n'.join(err)


def insertion_sort_alt():
    n = int(input())
    arr = list(map(int, input().split()))
    last_arr = arr.copy()
    res = []
    for i in range(1, n):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            if last_arr != arr:
                res.append(' '.join(list(map(str, arr))))
            arr[j + 1] = arr[j]
            j -= 1
            last_arr = arr.copy()
        arr[j + 1] = tmp
    res.append(' '.join(list(map(str, arr))))
    print('\n'.join(res))


def sort_wat(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def insertion():
    n = int(input())
    arr = input().split()
    number, index = input().split()
    arr.insert(int(index) - 1, number)
    print(' '.join(arr))


def ins_sort():
    n = int(input())
    data = list(map(int, input().split()))
    prev = data.copy()
    for i in range(n):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            if data != prev:
                print(*data)
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    print(*data)


# ins_sort()


def count_sort(arr):
    cnt = [0] * 10
    for el in arr:
        cnt[el] += 1
    arr = []
    for i in range(len(cnt)):
        arr += [i] * cnt[i]
    return arr


def stripper():
    s = input()
    arr = [int(i) for i in s if i.isdigit()]
    cnt = [0] * 10
    for el in arr:
        cnt[el] += 1
    arr = []
    for i in range(len(cnt)):
        arr += [i] * cnt[i]
    print(int(''.join(map(str, arr[::-1]))))


def merge_lines():
    x = int(input())
    a, b, = [0, 1, 4], []
    for i in range(x):
        a.append(i ** 2)
        b.append(i ** 3)

    print(sorted(list(set(a + b)))[x])


def merge_test():
    a = [i ** 2 for i in range(10 ** 6)]
    b = [i ** 3 for i in range(10 ** 6)]
    arr = sorted(list(set(a + b)))
    wrong_val = []
    for i in range(10 ** 6):
        if merge_lines(i) != arr[i]:
            wrong_val.append(i)
            with open('out.txt', 'a') as f_r:
                f_r.write('err: {true} != {ans} @ {x} \n'.format(true=arr[i], ans=merge_lines(i), x=i))
    with open('out.txt', 'a') as f_r:
        f_r.write(*list(map(str, wrong_val)))


print(merge_lines())


def merge_sort():
    n = int(input())
    arr = list(map(int, input().split()))

    def merge(a, b):
        res = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        res.extend(a[i:])
        res.extend(b[j:])
        return res

    def msort(a):
        if len(a) <= 1:
            return a
        k = len(a) // 2
        return merge(msort(a[:k]), msort(a[k:]))

    print(msort(arr))


def large_number():
    from functools import cmp_to_key
    n = int(input())
    a = [input() for _ in range(n)]

    print(''.join(sorted(a, key=cmp_to_key(lambda x, y: -1 if x + y > y + x else x + y != y + x))))


def sim_arr():
    f_len = int(input())
    first = list(map(int, input().split()))
    s_len = int(input())
    second = list(map(int, input().split()))
    print('YES' if set(first) == set(second) else 'NO')


def num_sort():
    n = int(input())
    print(*(sorted(list(map(int, input().split())), key=lambda x: sum(map(int, str(x))), reverse=True)))


def socks():
    res = []
    length, n, m = tuple(map(int, input().split()))
    arr = [0] * (length + 1)
    for i in range(n):
        left, right = map(int, input().split())
        for j in range(left, right + 1):
            arr[j] += 1
    for _ in range(m):
        res.append(arr[int(input())])
    print('\n'.join(map(str, res)))
    # print(*res, sep="\n") - правильно так


def keyboard():
    n, c = int(input()), tuple(map(int, input().split()))
    k, p = int(input()), tuple(map(int, input().split()))
    arr = [0] * n

    for i in range(k):
        arr[p[i] - 1] += 1
    for j in range(n):
        print('yes' if arr[j] > c[j] else 'no')


def olimp():
    def compare(a, b):
        if a[1] == b[1]:
            return a[0] < b[0]
        else:
            return a[1] > b[1]

    res = []
    n = int(input())
    for _ in range(n):
        arr = [int(s) for s in input().split()]
        res.append(arr)
    for i in range(1, len(res)):
        tmp = res[i]
        j = i - 1
        while j >= 0 and compare(tmp, res[j]):
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = tmp
    for c in res:
        print(*c)


def insertion_sort(a):
    n = int(input())
    data = list(map(int, input().split()))
    data_prev = data.copy()
    for i in range(n):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            # print(*data)
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        if data != data_prev:
            print(*data)
        data_prev = data.copy()
