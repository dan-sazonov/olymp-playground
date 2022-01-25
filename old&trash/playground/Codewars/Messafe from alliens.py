'''
Test.assert_equals(decode("]()]|_]|_]][-]|-|]"), 'hello')
Test.assert_equals(decode('{|^{|{{|_{]3{'),'blip')
Test.assert_equals(decode('..[-.|_.|^....().[-.|^.__..|)...|.|^.|_|..~|~._\\~.__...[-..|.|)..'),'die stupid people')
Test.assert_equals(decode('}/\\}~|~}/\\}/<}__}|)}}}[-}~|~}/\\}(}|}|_}|^}|_|}|)}__}|)}}}|\\|}|}/=}__}()}}}~|~}__}`/}/?}}~|~}') ,'try to find duplicated kata')
'''


def decode(m):
    return m.replace('|', ' ')


print(decode(']()]|_]|_]][-]|-|]'))
print(decode('{|^{|{{|_{]3{'))
