arr = list(map(int, open('17-243.txt').readlines()))
summ = 0
count = 0
m = 20001

for i in arr:
    if i % 35 == 0:
        summ += sum(map(int, str(i)))

for j in range(len(arr) - 1):
    a = arr[j]
    b = arr[j + 1]
    if a > summ >= b and hex(b)[-2:] == 'ef':
        count += 1
        m = min(m, a + b)
    if b > summ >= a and hex(a)[-2:] == 'ef':
        count += 1
        m = min(m, a + b)

print(count, m)
