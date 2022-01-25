laws = []
for _ in range(int(input())):
    action, party = input().split()

    if action == 'Add':
        laws.append(party)
    elif action == 'Vote' and not laws:
        print('NO')
        break
    elif action == 'Vote' and laws[-1] != party:
        print('NO')
        break
    elif action == 'Vote' and laws[-1] == party:
        laws.pop()
else:
    print('Yes')
