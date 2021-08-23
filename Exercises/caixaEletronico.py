# -*- coding: utf-8 -*-
import math

print('-=-'*10)
print('        BANCO DevLinK        ')
print('-=-'*10)

valor = float(input('Quanto você quer sacar? '))

real = valor - valor%1
cemR = cinqR = vinteR = dezR = cincoR = doisR = umR = 0

while real - 100 >= 0:
    real -= 100
    cemR += 1
while real - 50 >= 0:
    real -= 50
    cinqR += 1
while real - 20 >= 0:
    real -= 20
    vinteR += 1
while real - 10 >= 0:
    real -= 10
    dezR += 1
while real - 5 >= 0:
    real -= 5
    cincoR += 1
while real - 2 >= 0:
    real -= 2
    doisR += 1
while real - 1 >= 0:
    real -= 1
    umR += 1

centavo = valor%1 
cinqC = vinteCincoC = dezC = cincoC = umC = 0

while centavo - 0.50 >= 0:
    centavo -= 0.50
    cinqC += 1
while centavo - 0.25 >= 0:
    centavo -= 0.25
    vinteCincoC += 1
while centavo - 0.10 >= 0:
    centavo -= 0.10
    dezC += 1
while centavo - 0.05 >= 0:
    centavo -= 0.05
    cincoC += 1
while centavo - 0.01 >= 0:
    centavo -= 0.01
    umC += 1
    
print(f'{cemR} CÉDULAS DE R$ 100.00') if cemR >= 1 else print('-'*30)
print(f'{cinqR} CÉDULAS DE R$ 50.00') if cinqR >= 1 else print('-'*30)
print(f'{vinteR} CÉDULAS DE R$ 20.00') if vinteR >= 1 else print('-'*30)
print(f'{dezR} CÉDULAS DE R$ 10.00') if dezR >= 1 else print('-'*30)
print(f'{cincoR} CÉDULAS DE R$ 5.00') if cincoR >= 1 else print('-'*30)
print(f'{doisR} CÉDULAS DE R$ 2.00') if doisR >= 1 else print('-'*30)
print(f'{umR} MOEDAS DE R$ 1.00') if umR >= 1 else print('-'*30)
print(f'{cinqC} MOEDAS DE R$ 0.50') if cinqC >= 1 else print('-'*30)
print(f'{vinteCincoC} MOEDAS DE R$ 0.25') if vinteCincoC >= 1 else print('-'*30)
print(f'{dezC} MOEDAS DE R$ 0.10') if dezC >= 1 else print('-'*30)
print(f'{cincoC} MOEDAS DE R$ 0.05') if cincoC >= 1 else print('-'*30)
print(f'{umC} MOEDAS DE R$ 0.01') if umC >= 1 else print('-'*30)