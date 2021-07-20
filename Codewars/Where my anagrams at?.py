from collections import Counter

def anagrams(word, words):
    count = Counter(word)
    ans = []

    for i in words:
        print(i, count, Counter(i))
        if count == Counter(i):
            ans.append(i)
    return ans


print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
