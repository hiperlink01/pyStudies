print('-=-'*10)
print('SOCCER PLAYERS')
print('-=-'*10)

allP = []
player = {}
games = []

while True:

    player['Name'] = input('Player´s name: ').strip().title()
    games.append(player['Name'])

    m = int(input('Matches played: '))

    for i in range(0, m):
        games.append(int(input(f'Number of goals in match {i+1}: ')))

    allP.append(games[:])
    games.clear()

    yn = input('\nContinue? [Y/N] ').strip().upper()

    while yn != 'Y' and yn != 'N':
        yn = input('Invalid entry. Continue? [Y/N] ').strip().upper()
    
    if yn == 'N': break
    print('-=-'*10)

print('Number', end=' '*5)
print('Name', end=' '*10)
print('Goals', end=' '*15)
print('Goal Sum')
print('-=-'*20)
for i, c in enumerate(allP):
    print(i, end=' '*10)
    print(c[0], end=' '*4)
    print(c[1:], end=' '*15)
    print(sum(c[1:]))
print('-=-'*20)

while True:
    select = int(input('Type player´s number to show info about. Type negative number to stop.'))
    if select < 0: break

    while select > len(allP) - 1:
        print('-=-'*10)

        print('Invalid entry.')
        select = int(input('Type player´s number to show info about. Type negative number to stop.'))
    
    print('-=-'*10)
    print(f'{allP[select][0]}´s information:')

    for c, i in enumerate(allP[select][1:]):
        print(f'{i} goals in match {c+1}.')
        
    print('-=-'*10)