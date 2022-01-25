n, l, v, k, s = map(float, input().split())
v /= 100

t1 = l / v + k
times = s // t1
stops = times * k
length = (s - stops) * v
ans = ((8 * n + length) ** 2) / 16

print(round(ans, 2))
