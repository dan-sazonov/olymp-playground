n = int(input())
wo_zeroes = []
end_zeroes = []
start_zeroes = []


def descending_zeroes(num):
    return num.count('0')


for _ in range(n):
    digit = input()
    if digit.startswith('0'):
        start_zeroes.append(digit)
    elif digit.endswith('0'):
        end_zeroes.append(digit)
    else:
        wo_zeroes.append(digit)

wo_zeroes.sort(reverse=True)
end_zeroes.sort(reverse=True)
start_zeroes.sort(key=lambda x: x.count('0'), reverse=True)

print(*wo_zeroes, *end_zeroes, *start_zeroes, sep='')
