Fin = open("input.in")
Fout = open("output.txt", "w")
str = Fin.readline().split()

d = int(str[0])
a = int(str[1])
k = '0'
if d > a:
    k = d
else:
    k = a

print(k)