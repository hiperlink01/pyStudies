print('-=-'*6)
print('{: ^18}'.format('MATRIX CREATOR'))
print('-=-'*6)

matrix = [[0, 1, 2],
          [0, 1, 2],
          [0, 1, 2]]

for c in range(3):
    for i in range(3):
         matrix[c][i] = int(input(f'Insert a number in [{c}, {i}] '))

print('-=-'*10)

print('3x3 MATRIX CREATED: \n')
for c in matrix:
    for i in c: print(f'[{i:>5}]', end=' ')
    print('\n')

print('Thank you very much!')