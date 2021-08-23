# -*- coding: utf-8 -*-
sn = 's'
numLis = []

while sn != 'n':
    num = int(input('Digite um número: '))
    numLis.append(num)
    
    sn = str(input('Quer continuar? [S/N]: ').strip() ).lower()
    while sn != 's' and sn != 'n':
        print('Opção inválida.')
        sn = str(input('Quer continuar? [S/N]: ').strip() ).lower()
        
print('Você digitou {} números, e a média entre eles é {:.3f}.'.format(len(numLis), sum(numLis)/len(numLis)))
print('O menor valor foi {}, e o maior foi {}.'.format(min(numLis), max(numLis)) )