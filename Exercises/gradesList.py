from time import sleep

print('-=-'*7)
print('GRADES REGISTERING')
print('-=-'*7)

database = [[], [], []]

yn = 'Y'

while yn != 'N':

    database[0].append(input('Name: ').strip().title())
    database[1].append(float(input('Grade 1: ')))
    database[2].append(float(input('Grade 2: ')))

    print('-'*20)
    yn = input('Continue? [Y/N] ').strip().upper()
    while yn not in 'YN':
        yn = input('Invalid entry. Continue? [Y/N] ').strip().upper()
    if yn == 'Y': print('-'*20)

print('R.N.', ' '*10, 'Name', ' '*17, 'Grades average')
print('-=-'*18)
for i in range(0, len(database[0])): 
    print(i, end=' -  ')
    print('{:^28}'.format(database[0][i]), end='')
    print('{:>20}'.format( (database[1][i]+database[2][i])/2 ))
print('-=-'*18)

while True:
    rn = int(input('Type the R.N. to show the student´s grades / Negative number to finish the program: ' ))
    if rn < 0: break

    print('-'*25)
    print(f'The grades of {database[0][rn]}: \n1- {database[1][rn]} \n2- {database[2][rn]}')
    print('-'*25)

print('\nfinishing...')
sleep(1)
print('Please come again!')