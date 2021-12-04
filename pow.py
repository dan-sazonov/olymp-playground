from time import time

count = 0


def name_decode(name: str) -> int:
    ans = []
    for letter in name:
        tmp = str(ord(letter) - 1071)
        ans.append(tmp if len(tmp) == 2 else f'0{tmp}')
    return int(''.join(ans))


def pow_b(a, n):
    if not n:
        return 1
    if n % 2 == 1:
        return pow_b(a, n - 1) * a

    b = pow_b(a, n / 2)

    # global count
    # print(count, b)
    # count += 1

    return (b * b) % 10000


# print(pow_b(7, 50) % 10000)
# print(pow_b(7, 1024) % 10000)
# print(pow_b(7, 2047) % 10000)
# start1 = time()
print(pow(7081012, 999599) % 10000)
# start2=time()
# print(pow_b(7081012, 999599) % 10000)
start = time()
print(pow_b(name_decode('даниил'), 999599) % 10000)
print(time() - start)
# print(start2-start1, time()-start2)
