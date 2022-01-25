def cycle_calc(number):
    ans = 1
    for c in range(1, number + 1):
        ans *= c
    return ans


def recursion_calc(number):
    if number == 1:
        return 1
    else:
        return number * recursion_calc(number - 1)


number = int(input())
print(cycle_calc(number), recursion_calc(number))
