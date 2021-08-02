n = int(input())
ans = []
div = 2

while n:
    ans.append(n % div)
    n //= div
    div += 1

print(*ans[::-1], sep='')
