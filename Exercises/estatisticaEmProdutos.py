# -*- coding: utf-8 -*-
print('!'*30)
print('     Loja SUPER BARATÃO     ')
print('!'*30)

lisProdutos = []
lisPrecos = []
precMil = 0

while True:
    
    print('='*30)
    
    lisProdutos.append(str(input('Nome do produto: ').strip() ).title())
    precos = float(input('Preço: R$ '))
    if precos >= 1000:
        precMil += 1
        lisPrecos.append(precos)
    else:
        lisPrecos.append(precos)
        
    print('='*30)
    
    sn = str(input('Quer continuar? [S/N] ').strip() ).upper()
    
    while sn != 'N' and sn != 'S':
        print('Opção inválida.')
        sn = str(input('Quer continuar? [S/N] ').strip() ).upper()
        
    if sn == 'N':
        break

print(f'TOTAL DA COMPRA: {sum(lisPrecos):.2f}')
print(f'{precMil} produtos custam mais do que R$ 1000.00')
print(f'O produto mais barato foi "{lisProdutos[lisPrecos.index(min(lisPrecos))]}" que custa R$ {min(lisPrecos):.2f}')
