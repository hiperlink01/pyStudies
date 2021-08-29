from random import randint

print('-=-'*7)
print(' MEGA SENA GENERATOR')
print('-=-'*7)

game = [0]
am = int(input('How many games you want to generate? '))

print('-=-'*12)

for i in range(1, am+1):
    for c in range(6):
        num = randint(1, 61)
        while num in game:
            num = randint(1, 61)
        game.append(num)
        
    print(f'Set {i}:', sorted(game[1:7]))
    del game[1:7]

print('-=-'*4)
print(' Good luck!')
print('-=-'*4)