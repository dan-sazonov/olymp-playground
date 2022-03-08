arr = list(map(int, open('17-1.txt').readlines()))
avr = sum(arr) / len(arr)
count = 0
m = -20001

for i in range(len(arr) -1):
    if arr[i] > avr or arr[i+1] > avr:
        count += 1
        m = max(m, arr[i] + arr[i+1])

print(count, m)

