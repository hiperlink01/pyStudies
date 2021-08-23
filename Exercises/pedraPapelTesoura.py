#-*- coding: utf-8 -*-

import random
vMaq = 0
vJog = 0

while vMaq + vJog < 3 and vMaq < 2 and vJog < 2:
   
    maq = random.randrange(0, 3)
    jog = int(input('Digite 0 para PEDRA, 1 para PAPEL, 2 para TESOURA: '))

    if jog > 2:
        print('Opção inválida. Tente novamente.')
        
    elif maq == 0:
        print('A máquina escolheu pedra.')
        if jog == 1:
            print('Papel embrulha pedra. Você venceu!')
            vJog += 1 
        elif jog == 2:
            print('Tesoura é destruída por pedra. Você perdeu.')
            vMaq += 1 
        elif jog == maq:
            print('A máquina e você escolheram pedra! Tente novamente.')
            
    elif maq == 1:
        print('A máquina escolheu papel.')
        if jog == 0:
            print('Pedra é embrulhada por papel. Você perdeu.')
            vMaq += 1 
        elif jog == 2:
            print('Tesoura corta papel. Você venceu!')
            vJog += 1 
        elif jog == maq:
            print('A máquina e você escolheram papel! Tente novamente.')
            
    elif maq == 2:
        print('A máquina escolheu tesoura.')
        if jog == 0:
            print('Pedra destrói tesoura. Você venceu!')
            vJog += 1
        elif jog == 1:
            print('Papel é cortado por tesoura. Você perdeu.')
            vMaq += 1 
        elif jog == maq:
            print('A máquina e você escolheram tesoura! Tente novamente.')
            
    print('MÁQUINA: {} PONTOS'.format(vMaq))
    print('-'*20)
    print('JOGADOR: {} PONTOS'.format(vJog))
    print('='*20)
    
if vMaq > vJog:
    print("A máquina venceu!")
elif vJog > vMaq:
    print("Você ganhou o jogo!")