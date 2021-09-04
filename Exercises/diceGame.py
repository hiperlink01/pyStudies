from time import sleep
from random import randint
from operator import itemgetter

print('-=-'*5)
print('DICE GAME!')
print('-=-'*5)

results = {'Player 1': randint(1, 6), 
           'Player 2': randint(1, 6),
           'Player 3': randint(1, 6),
           'Player 4': randint(1, 6)}

for k, v in results.items():
    print(f'{k} got {v}.')
    sleep(1)

print('-=-'*10)
sleep(1.5)

print('RANKING')
ranking = list(sorted(results.items(), key=itemgetter(1), reverse=True))

for i, v in enumerate(ranking):
    print(f'{i+1} Place: {v[0]} (Got {v[1]})')

print('-=-'*10)