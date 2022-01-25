import math

n = int(input())
health = list(map(int, input().split()))
power = int(input())
left = 0
right = max(health)

while right - left > 1:
    m = (right + left) // 2
    if sum(map(lambda h: math.ceil(h / m), health)) <= power:
        right = m
    else:
        left = m

print(right)
