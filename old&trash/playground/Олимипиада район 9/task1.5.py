n = float(open('input.in').readline().split()[0])
l = float(open('input.in').readline().split()[1])
v = float(open('input.in').readline().split()[2])
k = float(open('input.in').readline().split()[3])
s = float(open('input.in').readline().split()[4])

time = l / v + k    #время одного перехода
ans = s / time  #переходов
length = l - (s - ans * k) * v
d = (l / 4) + (2 * n) * 100
print(d ** 2)