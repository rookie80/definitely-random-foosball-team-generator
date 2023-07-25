import random

# Set this variable to True to rig the results for Anthony and Robert to be teammates.
rig_results = True

teams = []
with open("players.txt", 'r') as f:
    ex_players = []
    new_players = []
    for line in f.read().split('\n'):
        if line == '':
            continue
        player, experienced = line.split(' ')
        if int(experienced):
            ex_players.append(player)
        else:
            new_players.append(player)

    if rig_results and 'Anthony' in ex_players and 'Robert' in ex_players:
        ex_players.remove('Anthony')
        ex_players.remove('Robert')
        teams.append(['Anthony', 'Robert'])

    print("Total players: " + str(len(ex_players) + len(new_players)))
    # print(ex_players)
    # print(new_players)

    while len(ex_players) > 1 or len(new_players) > 1:
        if len(ex_players) > 0 and len(new_players) > 0:
            member1 = random.choice(ex_players)
            member2 = random.choice(new_players)
            teams.append([member1, member2])
            ex_players.pop(ex_players.index(member1))
            new_players.pop(new_players.index(member2))
        elif len(new_players) > 1:
            member1 = random.choice(new_players)
            new_players.pop(new_players.index(member1))
            member2 = random.choice(new_players)
            teams.append([member1, member2])
            new_players.pop(new_players.index(member2))
        elif len(ex_players) > 1:
            member1 = random.choice(ex_players)
            ex_players.pop(ex_players.index(member1))
            member2 = random.choice(ex_players)
            teams.append([member1, member2])
            ex_players.pop(ex_players.index(member2))

    if len(new_players) > 0:
        print("Unfortunate soul is: " + new_players.pop())
    if len(ex_players) > 0:
        print("Unfortunate soul is: " + ex_players.pop())

    print("Teams are: ")
    for i in range(len(teams)):
        team = random.choice(teams)
        teams.pop(teams.index(team))
        print(team[0] + ' ' + team[1])