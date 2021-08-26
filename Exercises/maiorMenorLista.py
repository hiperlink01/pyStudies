# -*- coding: UTF-8 -*-

numeros = []
parar = 'N'

while True:
    numeros.append(int(input('Digite um número.')))
    
    parar = input('Quer parar? Digite [S] para parar. ').strip().upper()
    if parar == 'S':
        break

print(f'Os números foram: {numeros}.')

print(f'O maior valor inserido foi {max(numeros)}, \
{numeros.count(max(numeros))} vezes, e está nas posições:', end=' ')
for i in range(0, len(numeros)):
    if numeros[i] == max(numeros):
        print(f'[{i}]', end=' ')

print(f'O menor valor inserido foi {min(numeros)}, \
{numeros.count(min(numeros))} vezes, e está nas posições:', end=' ')
for i in range(0, len(numeros)):
    if numeros[i] == min(numeros):
        print(f'[{i}]', end=' ')