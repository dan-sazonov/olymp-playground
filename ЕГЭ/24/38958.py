c = 0
m = 0
a_count = 0

for i in open('38958.txt').readlines()[0]:
    if a_count == 2:
        m = max(c,m)
        c = 0
        a_count=0
        continue
    if i == 'A':
        a_count += 1
    c += 1


m = max(c,m)
print(m)


