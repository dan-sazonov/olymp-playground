def smallest(a):
    inf = int(2e9) + 1
    n = len(a)
    a = [-inf] + a + [-inf]
    ans = [0] * (n + 2)
    st = [0]
    for i in range(1, n + 2):
        while a[st[-1]] > a[i]:
            ans[st.pop()] = i
        st.append(i)
    print(*ans[1:-1])
    return ans[1:-1]


smallest([3, 6, 8, 4, 2, 5])  # 5 4 4 5 7 7
