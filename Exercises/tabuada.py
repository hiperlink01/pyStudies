# -*- coding: utf-8 -*-
while True:
    
    num = int(input('Digite um número para mostrar sua tabuada: '))
    if num == 0:
        break
    
    vzs = int(input('Quantos produtos você quer mostrar? '))
    
    print('='*50)
    for i in range (1, vzs+1):
        print(f'{num} x {i} = {num*i}')
    print('='*50)
    
print('PPROGRAMA ENCERRADO. Muito obrigado!')