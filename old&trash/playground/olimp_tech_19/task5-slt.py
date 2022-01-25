str_new = ''
input_one = input()
leng, num = input_one.split()
leng = int(leng)
num = int(num)
str_one = input()
str_two = input()
if num == leng:
    for i in range(leng):
        str_new = str_new + chr(ord(str_one[i]) + ord(str_two[i]) // 2 + ord(str_one[i]))
    print(str_new)
else:
    while num != leng:
        for i in range(leng):
            if num == leng:
                break
            if str_one[i] == str_two[i]:
                str_new = str_new + str_one[i]
                num += 1
            else:
                str_new = str_new + chr(ord(str_one[i]) + ord(str_two[i]) // 2 + ord(str_one[i]))
    if len(str_new) != leng:
        for i in range(leng - len(str_new)):
            str_new = str_new + chr(ord(str_one[i]) + ord(str_two[i]) // 2 + ord(str_one[i]))
    print(str_new)  # python
# не работает
