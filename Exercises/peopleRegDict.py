master = []
data = {}
ageSum = 0

while True:
    print('-=-'*10)

    data['Name'] = input('Name: ').strip().title()

    data['Sex'] = input('Sex [M/F]: ').strip().upper()
    while data['Sex'] != 'M' and data['Sex'] != 'F':
        print('Invalid entry. Please type [M] or [F].')
        data['Sex'] = input('Sex [M/F]: ').strip().upper()
    
    data['Age'] = int(input('Age: '))

    master.append(data.copy())
    
    yn = input('Continue? [Y/N] ').strip().upper()
    while yn != 'Y' and yn != 'N':
        print('Invalid entry. Please type [Y] or [N].')
        yn = input('Continue? [Y/N] ').strip().upper()

    if yn == 'N': break

for n, c in enumerate(master):
    if c['Age'] == master[n]['Age']: ageSum += c['Age'] 

print(f'\nThere are {len(master)} people registered.')

print('\nThe average between the ages is', ageSum/len(master))

if len(master) > 1:
    print('\nPeople above average:', end=' ')
    for c in master: 
        if c['Age'] > ageSum/len(master): print(c['Name'])

print('\nFemales registered:', end=' ')
for c in master: 
    if c['Sex'] == 'F': print(c['Name'])

print('-=-'*10)