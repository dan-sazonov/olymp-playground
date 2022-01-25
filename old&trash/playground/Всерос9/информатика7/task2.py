a = 2 * 10 ** 9
b = 2 * 10 ** 9

sum_odd = 0
sum_even = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        sum_odd += i
    else:
        sum_even += i

print(sum_odd - sum_even)