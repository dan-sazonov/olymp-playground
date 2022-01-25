# 60 баллов, 100 - informatics 111953
n = int(input())
n += 1

while str(n) != str(n)[::-1]:
    n += 1

print(n)
