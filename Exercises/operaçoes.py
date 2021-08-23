# -*- coding: utf-8 -*-

num1=float(input('Digite o primeiro número: '))
num2=float(input('Digite o segundo número: '))
choice = 0

while choice != 5:
    print('='*30)
    print('[1] SOMA')
    print('[2] SUBTRAÇÃO')
    print('[3] MULTIPLICAÇÃO')
    print('[4] ESCOLHER NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    print('='*30)
    
    choice = int(input('Qual operação você deseja realizar? '))
    
    if choice == 1:
        print('{} + {} = {:.3f}'.format(num1, num2, num1+num2))
        
    elif choice == 2:
        print('{} - {} = {:.3f}'.format(num1, num2, num1-num2))
        
    elif choice == 3:
        print('{} x {} = {:.3f}'.format(num1, num2, num1*num2))
        
    elif choice == 4:
        num1=float(input('Troque o primeiro número: '))
        num2=float(input('Troque o segundo número: '))
        
    elif choice == 5:
        print('Muito obrigado por usar o programa!')
        
    else:
        print('Comando inválido.')