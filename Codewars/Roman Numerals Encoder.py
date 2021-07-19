def solution(n):
    numbers = {4: {'1': 'M'},
               3: {'1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'},
               2: {'1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'},
               1: {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}}
    ans = []
    category = len(str(n))

    for i in str(n):
        if category == 4:
            ans.append('M' * int(i))
        elif i != '0':
            ans.append(numbers[category][i])
        category -= 1
    return ''.join(ans)



print(solution(1889))
'''
test.assert_equals(solution(1),'I', "solution(1),'I'")
test.assert_equals(solution(4),'IV', "solution(4),'IV'")
test.assert_equals(solution(6),'VI', "solution(6),'VI'")
test.assert_equals(solution(14),'XIV', "solution(14),'XIV")
test.assert_equals(solution(21),'XXI', "solution(21),'XXI'")
test.assert_equals(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
test.assert_equals(solution(91),'XCI', "solution(91),'XCI'")
test.assert_equals(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
test.assert_equals(solution(1000), 'M', 'solution(1000), M')
test.assert_equals(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
test.assert_equals(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")
''''''
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
'''
