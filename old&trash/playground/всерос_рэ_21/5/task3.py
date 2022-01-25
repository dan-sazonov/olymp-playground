# wa. 113098 informatics
from itertools import combinations

s = input()
strange = 0


def find_substrings(string):
    out = set()
    for a, b in combinations(range(len(string) + 1), r=2):
        out.add(string[a:b])
    return out


def find_subsequence(string, sub_string=""):
    ans = []
    if len(string) == 0:
        ans.append(''.join(sub_string))
        return ''.join(ans)
    ans.append(find_subsequence(string[:-1], sub_string + string[-1]))
    ans.append(find_subsequence(string[:-1], sub_string))
    return str(ans).translate(str.maketrans({'[': '', ']': '', '"': '', '\'': ''}))


for i in tuple(find_substrings(s)):
    sub_str = find_substrings(i)
    sub_seq = set(find_subsequence(i).split(', '))
    sub_seq.discard('')
    if sub_seq == sub_str:
        strange += 1

print(find_subsequence(s))
