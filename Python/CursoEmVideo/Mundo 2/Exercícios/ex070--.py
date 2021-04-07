total = totmil = menor = cont = 0
barato=''
while True:
    prod=str(input('Nome do produto:'))
    preço=float(input('Preço: R$'))
    total += preço
    cont += 1
    if preço>1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = prod
    resp = ' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp=='N':
        break
print(f'{"Fim do programa":-^40}')
print(f'O total da compra foi R${total:10.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais foi {barato} e custa R${menor:.2f}.')

