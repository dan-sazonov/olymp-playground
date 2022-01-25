clients = dict()


def deposit(name, amount):
    if name in clients.keys():
        clients[name] += amount
    else:
        clients[name] = amount


def withdraw(name, amount):
    if name in clients.keys():
        clients[name] -= amount
    else:
        clients[name] = -amount


def transfer(name1, name2, amount):
    withdraw(name1, amount)
    deposit(name2, amount)


def income(p):
    for i in clients:
        if clients[i] > 0:
            clients[i] += int(clients[i] * (p / 100))


def balance(name):
    if name in clients.keys():
        print(clients[name])
    else:
        print('ERROR')


for _ in range(int(input())):
    ask = input().split()
    if ask[0] == 'DEPOSIT':
        deposit(ask[1], int(ask[2]))
    elif ask[0] == 'WITHDRAW':
        withdraw(ask[1], int(ask[2]))
    elif ask[0] == 'BALANCE':
        balance(ask[1])
    elif ask[0] == 'TRANSFER':
        transfer(ask[1], ask[2], int(ask[3]))
    elif ask[0] == 'INCOME':
        income(int(ask[1]))
