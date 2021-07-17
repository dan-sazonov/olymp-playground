def pig_it(text):
    return ' '.join(i[1:] + i[0] + 'ay' if i.isalpha() else i for i in text.split())


'''
Test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
Test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')
'''

print(pig_it('Hello world !'))