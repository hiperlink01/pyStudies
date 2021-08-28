print('-=-'*6)

print('WEIGHT REGISTERING')
print('-=-'*6)

people = []
info = []
yn = 'Y'

while yn != 'N':
    info.append(input('NAME: ').strip().title())
    info.append(float(input('WEIGHT: ')))
    people.append(info[:])
    info.clear()

    print('-'*15)

    yn = input('Continue? [Y/N] ').strip().upper()
    while yn != 'Y' and yn != 'N': yn = input('Invalid entry. \nContinue? [Y/N] ').strip().upper()

maxW = 0
maxWNames = []
for c in people: 
    if maxW < c[1]: 
        maxW = c[1]
        maxWNames = c[0]

minW = 999999
minWNames = []
for c in people: 
    if minW > c[1]: 
        minW = c[1]
        minWNames = c[0]

print('=='*20)

print(f'You made {len(people)} entries.')

if len(people) == 1:
    print(f'You registered {maxWNames} that weights: {maxW}')
else:
    print(f'People with the highest weight ({maxW} Kg) were: {maxWNames}')
    print(f'People with the lowest weight ({minW} Kg) were: {minWNames}')

print('Thank you very much!')

print('=='*20)
