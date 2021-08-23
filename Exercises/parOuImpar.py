# -*- coding: utf-8 -*-
from random import randint

vit = 0

print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-='*15)


while True:
    
    parImpar = str(input('Você quer par ou ímpar? [P/I]' ).strip() ).upper()
    
    dedoJog = int(input('... Ok. E quantos dedos você coloca? (0 a 10) '))
    dedoMaq = randint(0, 10)
    
    if parImpar != 'P' and parImpar != 'I':
        print('Opção inválida.')
        
    elif (dedoJog + dedoMaq) % 2 == 0:
        if parImpar == 'P':
            print(f'Você jogou {dedoJog} e a máquina jogou {dedoMaq}, que é {dedoJog+dedoMaq}. É PAR! Você ganhou!')
            vit += 1
            
        elif parImpar == 'I':
            print(f'Você jogou {dedoJog} e a máquina jogou {dedoMaq}, que é {dedoJog+dedoMaq}. É PAR! Você perdeu.')
            break
        
    elif (dedoJog + dedoMaq) % 2 != 0:    
        if parImpar == 'P':
            print(f'Você jogou {dedoJog} e a máquina jogou {dedoMaq}, que é {dedoJog+dedoMaq}. É ÍMPAR! Você perdeu.') 
            break
        
        elif parImpar == 'I':
            print(f'Você jogou {dedoJog} e a máquina jogou {dedoMaq}, que é {dedoJog+dedoMaq}. É ÍMPAR! Você ganhou!')
            vit += 1
            
print('GAMEOVER'*5)
print('Você ganhou 1 vez!') if vit == 1 else print(f'Você ganhou {vit} vezes!')