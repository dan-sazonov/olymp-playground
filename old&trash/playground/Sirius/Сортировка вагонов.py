n = int(input())
arr = list(map(int, input().split()))
stop = [2001]
track2 = [0]

while len(arr) > 0:
    stop_counter = out_counter = 0
    while arr and stop[0] > arr[0]:
        print(stop[-1], arr[0])
        stop.append(arr.pop(0))
        stop_counter += 1
    print(stop_counter)
    while arr and stop[-1] - arr[0] != 1:
        stop.pop()
        out_counter += 1
    print(out_counter)
