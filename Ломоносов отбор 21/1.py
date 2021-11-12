n = int(input())
length = n
nums = [(input(), i + 1) for i in range(n)]
unordered = True


def larger_than(a, b):
    a, b = a.lstrip(), b.lstrip()

    if not (a and b):
        return False

    if len(a) == len(b):
        a, b = a.swapcase(), b.swapcase()
        for i in range(len(a)):
            if ord(a[i]) < ord(b[i]):
                return True
        return False

    if a == b:
        return False
    elif a.isdigit() and b.isdigit():
        return int(a) > int(b)
    elif a.isdigit() and not b.isdigit():
        return False
    elif not a.isdigit() and b.isdigit():
        return True
    elif len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False

    return False


while unordered:
    unordered = False
    for i in range(n - 1):
        if nums[i][0] == nums[i + 1][0]:
            print('fuck')
            del nums[i + 1]
        if larger_than(nums[i][0], nums[i + 1][0]):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            unordered = True
    n -= 1

if length == 2:
    print(nums[0][1])
else:
    for i in range(length):
        print(nums[i][1])
