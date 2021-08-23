# -*- coding: utf-8 -*-

print('-'*30)
print('CADASTRE DADOS DE UMA PESSOA')
print('-'*30)

lisMai = lisMen = lisSexo = []

while True:
    
    idd = int(input('IDADE: '))
    if idd >= 18:
        lisMai = [idd] 
    else:
        lisMen = [idd]
    
    sexo = str(input('SEXO [M/F}: ').strip() ).upper()
    lisSexo = [sexo] if sexo == 'M' or sexo == 'F' else print('Opção inválida.')

    sn = str(input('Quer continuar? [S/N]: ').strip() ).upper()
    if sn == 'N':
        break
    elif sn  == 'S':
        print('-'*30)
        print('CADASTRE DADOS DE OUTRA PESSOA')
        print('-'*30)

print('TOTAL DE MAIORES DE IDADE:', len(lisMai) )
print('TOTAL DE MENORES DE IDADE:', len(lisMen) )
print('TOTAL DE HOMENS:', lisSexo.count('M'))
print('TOTAL DE MULHERES:', lisSexo.count('F'))
