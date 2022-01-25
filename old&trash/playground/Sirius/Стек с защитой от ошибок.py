stack = []

while True:
    s = input().split()
    command = s[0]
    val = s[-1]
    if command == 'exit':
        break
    elif command == 'push':
        stack.append(val)
        print('ok')
    elif command == 'size':
        print(len(stack))
    elif command == 'clear':
        stack = []
        print('ok')
    if command == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print('error')
    if command == 'back':
        if len(stack):
            print(stack[-1])
        else:
            print('error')
print('bye')
