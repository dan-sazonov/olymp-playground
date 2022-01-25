n = int(input())
correct = dict()
mistakes = 0


def find_accent(item):
    ans = []
    for j in range(len(item)):
        if item[j].isupper():
            ans.append(j)
    return ans if ans else [-1]


for _ in range(n):
    word = input()
    for j in range(len(word)):
        if word[j].isupper():
            if word.lower() in correct.keys():
                correct[word.lower()].append(j)
            else:
                correct[word.lower()] = [j]
            break

for i in input().split():
    accent = find_accent(i)
    if len(accent) > 1 or accent[-1] == -1:
        mistakes += 1
        continue
    if i.lower() not in correct.keys():
        continue
    if accent[-1] not in correct[i.lower()]:
        mistakes += 1

print(mistakes)
