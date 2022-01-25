n, k = map(int, input().split())
arr = list(map(int, input().split()))
l_max = r_max = s_max = 0
left = 0
right = 1 + k

while right < len(arr):
    if arr[left] + arr[right] > s_max:
        s_max = arr[left] + arr[right]
        l_max = left
        r_max = right
    left += 1
    right += 1

print(l_max + 1, r_max + 1)
