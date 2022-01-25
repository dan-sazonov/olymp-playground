n = int(input())
print(len(set(filter(lambda x: x <= n, [int(input()) for i in range(n)]))))
