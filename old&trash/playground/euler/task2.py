fib = [1, 2]
n = int(input())

while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])

print(sum(list(filter(lambda x: x % 2 == 0, fib))))
