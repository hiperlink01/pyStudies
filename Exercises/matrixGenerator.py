print('-=-'*6)
print('{: ^18}'.format('MATRIX CREATOR'))
print('-=-'*6)

matrix = [[0, 1, 2],
          [0, 1, 2],
          [0, 1, 2]]

for c in range(3):
    for i in range(3): 
        matrix[c][i] = int(input(f'Insert a number in [{c}, {i}] '))

evenSum = 0
col3sum = 0
for c in matrix:
    for column, i in enumerate(c):
        if i % 2 == 0: evenSum += i
        if column == 2: col3sum += i 

print('-=-'*10, end='\n')

print('3x3 MATRIX CREATED: \n')
for c in matrix:
    for i in c: print(f'[{i:>5}]', end=' ')
    print('\n')

print('-=-'*10)

print('Sum of even numbers:', evenSum)
print('Sum of the third column:', col3sum)
print('Highest value of the second line:', max(matrix[1]))