# -*- coding: utf-8 -*-
cont = 0
num = int(input('Digite um número para descobrir se ele é primo: '))

print('\033[m='*10)

for i in range (1, num+1):
    
    if num % i == 0:
        print('\033[m{}'.format(i), end=' ')
        cont += 1
        
    else:
        print('\033[33m{}'.format(i), end=' ')
        
print('\033[m='*10)

if cont <= 2:
    print('O número é primo, pois foi possível dividi-lo apenas {} vezes.'.format(cont))
else:
    print('O número não é primo, pois foi possível dividi-lo {} vezes.'.format(cont))