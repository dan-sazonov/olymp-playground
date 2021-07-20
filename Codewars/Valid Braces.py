def validBraces(string):
    reverse = {')':'(', ']':'[', '}':'{'}
    open = []

    for i in string:
        if i in {'(', '[', '{'}:
            open.append(i)
        elif open and i in {')', ']', '}'} and open[-1] == reverse[i]:
            open.pop()
    return not bool(open)

'''
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
'''
print(validBraces('(}'))
