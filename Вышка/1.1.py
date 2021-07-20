n = int(input())
train = []
cars = dict()

for _ in range(n):
    ask = input().split()

    if ask[0] == 'add':
        car = ask[2]
        nums = int(ask[1])
        train.extend([car] * nums)
        if car in cars.keys():
            cars[car] += nums
        else:
            cars[car] = nums

    elif ask[0] == 'delete':
        for _ in range(int(ask[1])):
            cars[train.pop()] -= 1
    elif ask[0] == 'get':
        if ask[1] in cars.keys():
            print(cars[ask[1]])
        else:
            print(0)
'''
7
add 10 oil
add 20 coal
add 5 oil
get coal
get oil
add 1 coal
get coal
'''
'''
6
add 5 oil
get coal
add 7 liverstock
delete 10
get oil
get liverstock
'''