operations = {'read': 'R', 'write': 'W', 'execute': 'X'}
files = dict()
log = []

for _ in range(int(input())):
    name, *rights = input().split()
    files[name] = rights

for _ in range(int(input())):
    action, file = input().split()
    log.append('OK' if operations[action] in files[file] else 'Access denied')

print(*log, sep='\n')
