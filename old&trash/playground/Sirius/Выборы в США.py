n = int(input())
electors = dict()
votes = dict()
winners = dict()
for _ in range(n):
    n = input().split()
    electors[n[0]] = int(n[1])
    votes[n[0]] = []

for _ in range(int(input())):
    s = input().split()
    votes[s[0]].append(s[1])

for i in votes:
    votes[i] = sorted(votes[i], key=lambda x: votes[i].count(x))
    if votes[i][-1] in winners.keys():
        winners[votes[i][-1]] += electors[i]
    else:
        winners[votes[i][-1]] = electors[i]

print(winners)
