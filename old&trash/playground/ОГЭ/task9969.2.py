# Напишите программу, которая в последовательности натуральных чисел определяет сумму всех таких чисел, которые кратны 4 и оканчиваются на 2

foo = input().split()
ans = 0
for c in foo:
    if int(c) == 0:
        break
    elif c[-1] == '2' and (int(c) % 4 == 0):
        ans += int(c)
    else:
        continue

print(ans)
