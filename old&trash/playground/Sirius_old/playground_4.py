def task1_4():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0

    total = sum(a[:k + 1])
    if total != m:
        for i in range(1, n - k):
            total += a[i + k] - a[i - 1]
            if total == m:
                res = i + 1
                break
    else:
        res = 1
    print(res)


def task1_1():
    input()
    arr = tuple(map(int, input().split()))
    i_best = j_best = i_min = 0

    for i in range(2, len(arr)):
        if arr[i - 1] < arr[i_min]:
            i_min = i - 1
        if 1 < (arr[i] / arr[i_min]) > (arr[j_best] / arr[i_best]):
            i_best, j_best = i_min, i

    print(i_best + 1 if i_best else 0, j_best + 1 if j_best else 0)


def task1_5():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    p = [0] * (n + 1)
    for i in range(1, n):
        if h[i] > h[i - 1]:
            p[i] = p[i - 1] + 1
        else:
            p[i] = p[i - 1]
    p.pop()
    for i in range(m):
        l, m = map(int, input().split())
        print(p[m - 1] - p[l - 1])


def task2_1():
    n = int(input()) + 2
    a = [-1, *map(int, input().split()), -1]
    ans = [0] * n
    stack = [0]

    for i in range(1, n):
        while a[stack[-1]] > a[i]:
            ans[stack.pop()] = i
        stack.append(i if i < n - 2 else -1)

    print(*map(lambda x: x - 1, ans[1:-1]))


def task1_6():
    n = int(input())
    arr = list(map(int, input().split()))

    left = [-1] * 3
    right = [-1] * 3
    p = index = 0
    max_length = 0
    max_index = -1

    for i in range(n):
        if left[index] < 0:
            left[index] = i
        p += arr[i]
        index = p % 3
        if left[index] >= 0:
            right[index] = i
            if i - left[index] + 1 > max_length:
                max_length = i - left[index] + 1
                max_index = index

    print(left[max_index] + 1, right[max_index] + 1 if max_index >= 0 else max_index)


def task2_4():
    from collections import deque

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    perspective = deque()
    for i in range(n):
        if i >= k and perspective[0] == i - k:
            perspective.popleft()
        while len(perspective) and arr[perspective[-1]] >= arr[i]:
            perspective.pop()
        perspective.append(i)
        if i >= k - 1:
            print(arr[perspective[0]])


def task2_2():
    inf = 2 * (10 ** 9) + 1
    a = list(map(int, input().split()))
    n = a[0]
    h = [-inf] + a[1:] + [-inf]
    ans = [[0, 0] for i in range(n + 2)]
    stack = [0]
    for i in range(1, n + 2):
        tmp = h[i]
        while h[stack[-1]] > tmp:
            ans[stack.pop()][1] = i
        stack.append(i)
    stack = [0]
    for i in range(n + 1, 0, -1):
        tmp = h[i]
        while h[stack[-1]] > tmp:
            ans[stack.pop()][0] = i
        stack.append(i)
    m = -inf
    for i in range(1, n + 1):
        s = h[i] * (ans[i][1] - ans[i][0] - 1)
        m = max(m, s)
    print(m)


def task1_3():
    n, x = map(int, input().split())
    ask = list(map(int, input().split()))
    sale = list(map(int, input().split()))
    ask_day = sell_day = -2
    amount = x
    min_a = ask[0]
    min_i = 0
    for i in range(n):
        if ((x // min_a) * sale[i] + x % min_a) > amount:
            amount = (x // min_a) * sale[i] + x % min_a
            ask_day = min_i
            sell_day = i
        if ask[i] < min_a:
            min_a = ask[i]
            min_i = i
    else:
        print(amount)
    print(ask_day + 1, sell_day + 1)


def task1_2():
    _, distance = map(int, input().split())
    cells = list(map(int, input().split()))
    max_a = max_a_i = max_sum = 0
    answer = 0

    for a_i, a in enumerate(cells[:-distance - 1]):
        b_i = a_i + distance + 1
        b = cells[b_i]
        if a > max_a:
            max_a = a
            max_a_i = a_i
        if max_a + b > max_sum:
            max_sum = max_a + b
            answer = (max_a_i, b_i)

    print(answer[0] + 1, answer[1] + 1)


def task2_6():
    n = int(input())
    a = list(map(int, input().split()))
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]
    s = [-1]
    for i in range(n - 1, -1, -1):
        while s[-1] != -1 and a[s[-1]] > a[i]:
            s.pop()
        if s[-1] == -1:
            right[i] = a[i] * (n - i)
        else:
            right[i] = right[s[-1]] + a[i] * (s[-1] - i)
        s.append(i)
    s = [-1]
    for i in range(n):
        while s[-1] != -1 and a[s[-1]] > a[i]:
            s.pop()
        if s[-1] == -1:
            left[i] = a[i] * (i + 1)
        else:
            left[i] = left[s[-1]] + a[i] * (i - s[-1])
        s.append(i)
    m = 0
    ind = -1
    for i in range(n):
        total = left[i] + right[i] - a[i]
        if total > m:
            m = total
            ind = i
    i = ind - 1
    j = ind + 1
    m1 = a[ind]
    m2 = a[ind]
    while i >= 0:
        if a[i] > m1:
            a[i] = m1
        else:
            m1 = a[i]
        i -= 1
    while j < n:
        if a[j] > m2:
            a[j] = m2
        else:
            m2 = a[j]
        j += 1
    print(*a)


def task1_7():
    n = int(input())
    a = []
    while True:
        for i in range(n):
            a.append(int(input()))
        if n == 2:
            print(1, 2, sep='\n')
            break
        ans = a[0]
        ans_l = ans_r = s = 0
        minus_pos = -1
        for j in range(n):
            s += a[j]
            if s > ans:
                ans = s
                ans_l = minus_pos + 1
                ans_r = j
            if s <= 0:
                s = 0
                minus_pos = j
        print(ans_l + 1, ans_r + 1, sep='\n')
        break


def task2_5():
    from collections import deque

    n, k = map(int, input().split())
    x, d, ssum = list(map(int, input().split())), deque(), 0
    b = [(0, 0) for i in range(n)]
    for i in range(n):
        ssum += x[i]
        if i >= k:
            ssum -= x[i - k]
            if d[0] == i - k:
                d.popleft()
            while len(d) and x[d[-1]] >= x[i]:
                d.pop()
            d.append(i)
            if i >= k - 1:
                nb = (b[i - k][0] + x[d[0]] * ssum, i - k + 2)
                b[i] = max(b[i - 1], nb, key=lambda x: x[0])
    i = n - 1

    d = deque()
    j = b[-1][1]
    d.appendleft(j)
    while i != 0:
        i -= 1
        j1 = b[i][1]
        if j - k >= j1 > 0:
            d.appendleft(j1)
            j = j1
    print(str(len(d)))
    print(" ".join(map(str, d)))
