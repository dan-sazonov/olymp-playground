ans = int(open('input.in').readline().split()[0])
b = int(open('input.in').readline().split()[1])
conv = []

while ans > 0:
    if ans < b:
        conv.append(ans)
        conv.reverse()
        break
    ans = ans // b
    conv.append(ans % b)

print(conv)