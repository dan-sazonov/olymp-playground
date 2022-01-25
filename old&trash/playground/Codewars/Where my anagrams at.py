def anagrams(word, words): return [i for i in words if sorted(i) == sorted(word)]


'''
Test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
Test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
'''

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
