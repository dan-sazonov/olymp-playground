n = int(input())
inf = int(10e9) + 1
a = [-inf, *map(int, input().split()), -inf]
st = [0]
ans = [0] * (n + 2)

for i in range(1, n + 2):
    while a[st[-1]] > a[i]:
        ans[st.pop()] = i
    st.append(i)

for j in ans[1:-1]:
    if j > n:
        print(-1, end=' ')
    else:
        print(j - 1, end=' ')
