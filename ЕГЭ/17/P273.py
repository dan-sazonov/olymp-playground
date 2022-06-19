# arr = [12, 18, 3, -15, 11, 16]
arr = list(map(int, open('17-273.txt')))
i_max = max(arr)
c = 0
el_max = -50000
el_min = 50000

for i in range(len(arr) - 2):
    if (arr[i] + arr[i+1] + arr[i+2]) < i_max:
        c += 1
        el_max = max(el_max, max(arr[i], arr[i+1], arr[i+2]))
        el_min = min(el_min, min(arr[i], arr[i+1], arr[i+2]))

print(c, el_min + el_max)
