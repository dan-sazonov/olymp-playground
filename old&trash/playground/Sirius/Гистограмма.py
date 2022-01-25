def max_rect(a):
    inf = 2 * (10 ** 9) + 1
    n = a[0]
    h = [-inf] + a + [-inf]
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

    print(ans)


max_rect([3, 6, 8, 4, 2, 5])


def max_rect_alt(a):
    n = len(a)
    min_left = [0] * (n + 2)
    min_right = [0] * (n + 2)
    inf = int(2e9) + 1

    a = [-inf] + a + [-inf]
    st = [0]
    for i in range(1, n + 2):
        print(i)
        while (a[st[-1]] < a[i]) and st:
            min_right[st.pop()] = i
        st.append(i)
    print(min_right[::-1])


max_rect_alt([3, 6, 8, 4, 2, 5])
