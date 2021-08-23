# -*- coding: utf-8 -*-
print('='*22)
print('SEQUÊNCIA DE FIBONACCI')
print('='*22)

termoMeio = 1
termoVelho = 0
cont = 1

quant = int(input('Quantos termos quer mostrar? '))

if quant >= 1:
    print('0', end=' -> ')
    
    while cont != quant:
        print(termoMeio, end=' -> ')
        termoNovo = termoVelho + termoMeio
        termoVelho = termoMeio
        termoMeio = termoNovo
        
        cont += 1
            
    print('...')

    print('\n Muito obrigado!')
    
else:
    print('\n Muito obrigado!')