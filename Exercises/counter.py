from time import sleep

def count(start, stop, step):

    sequence = []

    for i in range(start, stop, step):
        sequence.append(i)
    sequence.append(stop)

    print('-=-'*47)

    print(f'Counting from {start} to {stop}, {step} by {step}: ')
    for i in sequence:
        print(i, end=' -> ')
        sleep(0.25)
    print('...')
    
    print('-=-'*47)


count(0, 10, 1)
count(10, 0, -1)

print('Now it´s your turn!')

while True:

    s1 = int(input('Starting number: '))
    s2 = int(input('Stopping number: '))
    s0 = int(input('Step: '))

    count(s1, s2, s0)

    yn = input('Continue? [Y/N] ').strip().upper()
    while yn not in 'YN':
        print('Invalid entry.')
        yn = input('Continue? [Y/N] ').strip().upper()
    if yn == 'N': break

print('Please, come again!')