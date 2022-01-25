with open('input.txt') as f_read:
    foo = list(map(int, f_read.read().split()))
    print(foo)

teams = [i+1 for i in range(foo[0])]
t = 1
while len(teams) > 1:
    left_teams = []
    for i in range(0, len(teams), 2):
        if foo[t] == 1:
            left_teams.append(teams[i])
        else:
            left_teams.append(teams[i + 1])
        t += 1
    teams = left_teams

print(teams)
