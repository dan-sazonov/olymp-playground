operands = []

for i in input().split():
    if i.isdigit():
        operands.append(i)
    else:
        exp = operands.pop(-2) + i + operands.pop()
        operands.append(str(eval(exp)))

print(operands[-1])
