n = int(input())
maximal = sorted([int(input()) for _ in range(5)])

for _ in range(n - 5):
    x = int(input())
    for i in range(5):
        if maximal[i] < x:
            maximal[i] = x
            break

print(*sorted(maximal)[::-1])
