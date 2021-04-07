print(f'{" Caixa Chega Mais ":=^30}')
valor=int(input('Que valor você quer sacar?'))
céd = 50
total = valor
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}.')
        if céd==50:
            céd=20
        elif céd==20:
            céd=10
        elif céd==10:
            céd=5
        elif céd==5:
            céd=2
        totcéd = 0
        if total == 0:
            break
print('='*30)
print('Saque realizado com sucesso. Volte sempre!')
