def segment(a):
    n = len(a) + 1
    p = [0] * n
    m = int(input())
    for i in range(1, n):
        p[i] = p[i - 1] + a[i - 1]
    for j in range(m):
        left, right = map(int, input().split())
        print(p[right + 1] - p[left])


segment([0, 1, 2, 3, 4, 5, 6, 7, 8])  # 20
