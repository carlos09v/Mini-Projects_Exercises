print('$'*40)
print(f'{" Caixa SoNoDally ":=^40}')
print('$'*40)
print('Bem Vindo!')
saque=int(input('Qual o valor do saque?'))
céd = 100
total = saque
totalcéd = 0
while True:
    if total >= céd:
        total -= céd
        totalcéd += 1
    else:
        if totalcéd > 0:
           print(f'Total de {totalcéd} cédulas de R${céd}')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        totalcéd = 0
        if total == 0:
            break
print('='*30)
print('Saque realizado com SUCESSO. Volte sempre!')
