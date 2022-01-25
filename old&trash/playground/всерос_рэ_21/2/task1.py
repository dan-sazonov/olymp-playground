# 114038

l = int(input())
r = int(input())
a = int(input())
counter = 0

for i in range(l, r + 1):
    for j in range(i, r + 1):
        if l <= i < j <= r and (j - i) % a == 0:
            counter += 1

print(counter)
