n = int(input())
teams = [i + 1 for i in range(n)]
while len(teams) > 1:
    left_teams = []
    for i in range(0, len(teams), 2):
        if int(input()) == 1:
            left_teams.append(teams[i])
        else:
            left_teams.append(teams[i + 1])
    teams = left_teams
print(teams[0])
