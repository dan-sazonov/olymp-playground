arr = []

for i in open('35484.txt').readlines():
    arr.append(int(i))

arr_set = set(arr[1:])
arr_odd = []
avr_max = 0
c = 0

for i in range(1, len(arr)):
    if arr[i] % 2 == 0:
        arr_odd.append(arr[i])

for i in range(len(arr_odd)):
    for j in range(i, len(arr_odd)):
        avr = (arr_odd[i] + arr_odd[j]) // 2
        if (avr in arr_set) and (arr_odd[i] != arr_odd[j]):
            c += 1
            if avr >= avr_max:
                avr_max = avr

print(c, avr_max)
