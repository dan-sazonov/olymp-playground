def task2_1():
    n = set(map(int, input().split()))
    print(len(n))


def task2_2():
    ans = []
    for i in input():
        if i not in ans:
            ans.append(i)
    print(*ans, sep='')


def task1_2(d):
    opening = []
    sign_inverse = {')': '(', ']': '[', '}': '{'}

    for sign in input():
        if sign in ('(', '[', '{'):
            opening.append(sign)
        elif opening and sign_inverse[sign] != opening[-1]:
            print('no')
            break
        elif not opening:
            print('no')
            break
        else:
            opening.pop()
    else:
        print('no' if opening else 'yes')


def test1_2():
    print('test 1(y): ', task1_2('([])'), '\n')
    print('test 2(n): ', task1_2('{)'), '\n')
    print('test 3(n): ', task1_2(')(){}[]'), '\n')
    print('test 4(n): ', task1_2('(){}{}['), '\n')
    print('test 5(n): ', task1_2('](){}{}['), '\n')
    print('test 6(n): ', task1_2(']'), '\n')
    print('test 7(n): ', task1_2('['), '\n')


def task1_2_a():
    s = input()
    fit = {')': '(', ' } ': ' { ', ']': '['}
    st = []

    res = 'yes'
    for a in s:
        if st:
            if a in '( { [':
                st.append(a)
            elif a in ') } ]':
                d = st.pop()
                if fit[a] != d:
                    print(fit[a], d)
                    res = 'no'
                    break
        else:
            res = 'no'
            break

    if st:
        res = 'no'

    print(res)


def task1_3():
    string = input().split()
    operands = []

    for i in string:
        if i.isdigit():
            operands.append(i)
        else:
            exp = operands.pop(-2) + i + operands.pop(-1)
            operands.append(str(eval(exp)))

    print(*operands)


def task1_4():
    input()
    vans = list(map(int, input().split()))
    vans_amount = len(vans)

    vans = vans[::-1]
    temp, res = [], []
    track_1, track_2 = [0], [0]

    while True:
        temp.append(vans.pop())
        while temp and vans and temp[-1] == vans[-1] + 1:
            temp.append(vans.pop())
        if track_2 and vans and track_2[-1] + 1 == vans[-1]:
            temp.append(vans.pop())
        res.append((1, len(temp)))
        track_1.extend(temp)
        temp = []
        if track_2[-1] + 1 == track_1[-1]:
            temp.append(track_1.pop())
            while temp[-1] + 1 == track_1[-1]:
                temp.append(track_1.pop())
        if temp:
            res.append((2, len(temp)))
            track_2.extend(temp)
            temp = []
        if not vans:
            if temp:
                res.append((2, len(temp)))
                track_2.extend(temp)
            track_2.pop(0)
            if track_2 != list(range(1, vans_amount + 1)):
                res = 0
            break

    if not res:
        print(0)
    else:
        for a in res:
            print(*a)


def task1_1():
    stack = []
    command = ''

    while command != 'exit':
        command = input()
        if command.split()[0] == 'push':
            stack.append(command.split()[1])
            print('ok')
        elif command == 'size':
            print(len(stack))
        elif command == 'clear':
            stack.clear()
            print('ok')
        try:
            if command == 'pop':
                print(stack.pop())
            elif command == 'back':
                print(stack[-1])
        except IndexError:
            print('error')
    else:
        print('bye')


def task2_3():
    input()
    first_set = set(map(int, input().split()))
    input()
    second_set = set(map(int, input().split()))

    first_set ^= second_set
    print(len(first_set))
    print(*sorted(first_set))


def task2_4():
    input()
    t = set(list(map(int, input().split())))
    input()
    r = set(list(map(int, input().split())))
    input()
    t1 = set(list(map(int, input().split())))
    input()
    r1 = set(list(map(int, input().split())))

    if (t & t1) or r1 <= r:
        print(-1)
    else:
        teachers = t1 | t
        print(len(teachers))
        print(*sorted(teachers))
        r.add(min(r1 - r))
        print(len(r))
        print(*sorted(r))


def task1_7():
    first_pack = input().split()
    second_pack = input().split()
    move_counter = 0

    while first_pack and second_pack:
        move_counter += 1
        a, b = first_pack.pop(0), second_pack.pop(0)
        if a > b and (a, b) != ('9', '0') or (a, b) == ('0', '9'):
            first_pack.extend([a, b])
        else:
            second_pack.extend([a, b])
        if move_counter >= 10 ** 6:
            print('botva')
            break
    else:
        print('first' if first_pack else 'second', move_counter)


def task1_8():
    n = int(input())
    s = [[], []]  # s[0] ложим, s[1] удаляем

    for _ in range(n):
        a = int(input())
        if a:
            s[0].append(a)
        else:
            if s[0] or s[1]:
                if not s[1]:  # голова пустая
                    b = s[0].pop()
                    s[1] = [(b, b)]
                    while s[0]:
                        b = s[0].pop()
                        s[1].append((b, min(b, s[1][-1][1])))

                print(s[1].pop()[1])
            else:  # надо удалять, а оба пустые
                print(-1)


def task2_6():
    num_votes = {}
    for _ in range(int(input())):
        candidate, votes = input().split()
        num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)

    for candidate, votes in sorted(num_votes.items()):
        print(candidate, votes)


def task2_7():
    n, m = map(int, input().split())
    result = [0 for _ in range(n)]
    ans = dict()
    for _ in range(m):
        team, word = input().split()
        ans[word] = int(team)

    for word in ans:
        result[ans[word] - 1] += 1

    print(*result)


def task2_8():
    n = int(input())
    words = {}
    mistakes = 0

    for i in range(n):
        word = input()
        base_form = word.lower()
        if base_form not in words:
            words[base_form] = set()
        words[base_form].add(word)
    for word in input().split():
        base_form = word.lower()
        uppercase_counter = len([l for l in word if l.isupper()])
        if (base_form in words and word not in words[base_form]) or uppercase_counter != 1:
            mistakes += 1
    print(mistakes)


def task2_9():
    def find_depth(family, key):
        d = 0
        while family[key]:
            try:
                key = family[key]
                d += 1
            except KeyError:
                break
        return d

    n = int(input())
    tree = dict()
    for _ in range(n - 1):
        child, parent = input().split()
        tree[child] = parent
        if parent not in tree:
            tree[parent] = 0
    for name, _ in sorted(tree.items()):
        print(name, find_depth(tree, name))


def task2_10():
    n = int(input())
    castles = list()
    x = set()
    y = set()
    for i in range(n):
        castles.append(list(map(int, input().split())))
    castles.sort()
    for i in range(n - 1):
        if castles[i + 1][0] == castles[i][0] and castles[i + 1][1] > castles[i][1]:
            y.add(castles[i][1] + 1)
        else:
            x.add(castles[i][0] + 1)
    print(len(x) + len(y))
    for i in y:
        print('y %d' % i)
    for i in x:
        print('x %d' % i)


def task1_9():
    command = []
    deque = []

    while command != ['exit']:
        command = input().split()
        if command[0] == 'push_front':
            deque.insert(0, command[1])
            print('ok')
        elif command[0] == 'push_back':
            deque.append(command[1])
            print('ok')
        elif command[0] == 'pop_front':
            print(deque.pop(0) if deque else 'error')
        elif command[0] == 'pop_back':
            print(deque.pop(-1) if deque else 'error')
        elif command[0] == 'front':
            print(deque[0] if deque else 'error')
        elif command[0] == 'back':
            print(deque[-1] if deque else 'error')
        elif command[0] == 'size':
            print(len(deque))
        elif command[0] == 'clear':
            deque.clear()
            print('ok')
    else:
        print('bye')


def task2_5():
    def deposit(name, amount):
        bank[name] = bank.get(name, 0) + int(amount)

    def withdraw(name, amount):
        bank[name] = bank.get(name, 0) - int(amount)

    def balance(name):
        log.append(bank[name] if name in bank else 'ERROR')

    def income(percent):
        for i, j in bank.items():
            if j > 0:
                bank[i] = int(j * ((int(percent) / 100) + 1))

    def transfer(name1, name2, amount):
        bank[name1] = bank.get(name1, 0) - int(amount)
        bank[name2] = bank.get(name2, 0) + int(amount)

    bank = dict()
    log = []
    for _ in range(int(input())):
        line = input().split()
        if 'BALANCE' in line:
            balance(line[1])
        elif 'DEPOSIT' in line:
            deposit(line[1], line[2])
        elif 'WITHDRAW' in line:
            withdraw(line[1], line[2])
        elif 'INCOME' in line:
            income(line[1])
        elif 'TRANSFER' in line:
            transfer(*line[1:])
        else:
            withdraw(line[1], line[3])
            deposit(line[2], line[3])
    print(*log, sep='\n')


''''
7
DEPOSIT Ivanov 100
INCOME 5
BALANCE Ivanov
TRANSFER Ivanov Petrov 50
WITHDRAW Petrov 100
BALANCE Petrov
BALANCE Sidorov
'''


def task2_5_a():
    def deposit(name, amount):
        bank[name] = bank.get(name, 0) + int(amount)

    def withdraw(name, amount):
        bank[name] = bank.get(name, 0) - int(amount)

    def balance(name):
        if name not in bank:
            log.append('ERROR')
        else:
            log.append(bank[name])

    def income(percent):
        for k, v in bank.items():
            if v > 0:
                bank[k] = int(v * ((int(percent) / 100) + 1))

    def transfer(name1, name2, amount):
        bank[name1] = bank.get(name1, 0) - int(amount)
        bank[name2] = bank.get(name2, 0) + int(amount)

    bank = dict()
    log = []
    for _ in range(int(input())):
        line = input().split()
        if 'BALANCE' in line:
            balance(line[1])
        elif 'DEPOSIT' in line:
            deposit(line[1], line[2])
        elif 'WITHDRAW' in line:
            withdraw(line[1], line[2])
        elif 'INCOME' in line:
            income(line[1])
        elif 'TRANSFER' in line:
            transfer(*line[1:])
        else:
            withdraw(line[1], line[3])
            deposit(line[2], line[3])
    print(*log, sep='\n')


def task1_6():
    queue = []
    command = []

    while 'exit' not in command:
        command = input().split()
        if 'push' in command:
            queue.append(int(command[1]))
            print('ok')
        elif 'front' in command and queue:
            print(queue[0])
        elif 'front' in command and not queue:
            print('error')
        elif 'size' in command:
            print(len(queue))
        elif 'clear' in command:
            queue.clear()
            print('ok')
        elif 'pop' in command and queue:
            print(queue.pop(0))
        elif 'pop' in command and not queue:
            print('error')
    else:
        print('bye')


task1_6()
'''
size
push 1
size
push 2
size
push 3
size
exit
0
ok
1
ok
2
ok
3
bye
'''