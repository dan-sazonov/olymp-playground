foo = input().split()
ans = 0

def main(c):
    if (c % 4 == 0) and (c % 7 != 0) and c != 7:
        return True
    else:
        return False

for c in foo:
    if main(int(c)):
        ans += 1
    else:
        continue

print(ans)



def multiple(max):
    # Для тестов. Находит числа, кратные 4 и 7
    out = [':']
    iter = 0
    for c in range(1, max + 1):
        if (c % 4 == 0) and (c % 7) == 0:
            out.append(c)
            iter += 1
        else:
            continue
    return out
