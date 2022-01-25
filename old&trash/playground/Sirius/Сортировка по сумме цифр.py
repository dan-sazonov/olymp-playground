n = int(input())
a = list(map(int, input().split()))


def find_sum(num):
    res = 0
    for i in str(num):
        res += int(i)
    return res


print(sorted(a, key=find_sum, reverse=True))
