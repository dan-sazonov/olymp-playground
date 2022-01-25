n = int(input())
price = [0, 1, 1, 1, 1, 1, 1, 1]  # цены указаны начиная с нулевой ступеньки
a = 0  # нулевая ступенька
b = price[1]  # первая ступенька

for i in range(2, n + 1):
    a, b = b, min(a, b) + price[i]

print(b)
