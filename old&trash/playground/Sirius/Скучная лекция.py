s = list(input())
ans = dict()
length = len(s)


def let_cnt(x, n):
    if x > n / 2:
        x = n - x
    return n * x - x * x


for i in range(length):
    cnt = let_cnt(i + 1, length + 1)
    for j in range(i + 1, length):
        if s[j] == s[i]:
            cnt += let_cnt(j + 1, length + 1)
    if s[i] not in ans.keys():
        ans[s[i]] = cnt

for letter in sorted(ans.keys()):
    print(f'{letter}: {ans[letter]}')

# s = list(input())
# ans = dict()
#
#bwvfhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhiasruomsvoaiiiiiiiiiiiiiiiiiiiiiinbrwbvrrwopnbvtqwopvtbnriwopvbnrwopvbnwiopvbnwopitvbniwponbvitwropvbnbwvfhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhiasruomsvoaiiiiiiiiiiiiiiiiiiiiiinbrwbvrrwopnbvtqwopvtbnriwopvbnrwopvbnwiopvbnwopitvbniwponbvitwropvbnbwvfhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhiasruomsvoaiiiiiiiiiiiiiiiiiiiiiinbrwbvrrwopnbvtqwopvtbnriwopvbnrwopvbnwiopvbnwopitvbniwponbvitwropvbnbwvfhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhiasruomsvoaiiiiiiiiiiiiiiiiiiiiiinbrwbvrrwopnbvtqwopvtbnriwopvbnrwopvbnwiopvbnwopitvbniwponbvitwropvbnbwvfhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifhifh...
# def let_cnt(x, n):
#     if x > n / 2:
#         x = n - x
#     return n * x - x * x
#
#
# for i in range(len(s)):
#     cnt = let_cnt(i + 1, len(s) + 1)
#     for j in range(i + 1, len(s)):
#         if s[j] == s[i]:
#             cnt += let_cnt(j + 1, len(s) + 1)
#     if s[i] not in ans.keys():
#         ans[s[i]] = cnt
#
# for letter in sorted(ans.keys()):
#     print(f'{letter}: {ans[letter]}')
