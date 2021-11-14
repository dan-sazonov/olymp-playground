n, q = map(int, input().split())
arr = list(map(int, input().split()))
ans = []


def find_sum(l, d):
    tmp = arr[l - 1]
    step = d
    while l + step <= n:
        tmp += arr[l + step - 1]
        step += d
    return tmp


for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        arr[a - 1] = b
    else:
        ans.append(find_sum(a, b))

print(*ans, sep='\n')
