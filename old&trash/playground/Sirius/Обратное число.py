ans = []

for i in range(int(input())):
    p, a = map(int, input().split())
    ans.append(pow(a, p-2, p))

print(*ans, sep='\n')
