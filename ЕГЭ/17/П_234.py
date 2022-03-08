arr = list(map(int, open('17-1.txt').readlines()))
avr = sum(arr) / len(arr)
count = 0
m = -30001

for i in range(len(arr) - 2):
    if (arr[i] < avr or arr[i + 1] < avr or arr[i + 2] < avr) and \
            ('9' in str(arr[i])) and ('9' in str(arr[i + 1])) and ('9' in str(arr[i + 2])):
        count += 1
        m = max(m, arr[i] + arr[i + 1] + arr[i + 2])

print(count, m)
