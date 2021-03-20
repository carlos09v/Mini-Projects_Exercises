from time import sleep
print('=-'*20)
print(f'{"SUPIMPA & CIA":^40}')
print("-="*20)
lista = list()
total = total1 = 0
for c in range(0,10):
    print(f'<<< CADASTRANDO {c+1}º PRODUTO >>>')
    nome=str(input('Nome: ')).title().strip()
    preço=float(input('Preço: '))
    total += preço
    if nome not in lista:
        lista.append([nome,[preço]])
        print('Produto cadastrado com sucesso!')
    else: #BUG
        print('Produto duplicado! Não foi possível efetuar o cadastro.')
        print('Tente novamente!')
        nome = str(input('Nome: '))
    resp = ' '
    resp=str(input('Quer continuar o cadastro? [S/N]')).strip().upper()[0]
    while resp not in 'SN':
        print('Dado Inválido. Tente Novamente!')
        resp = str(input('Quer continuar o cadastro? [S/N]')).strip().upper()[0]
    if resp=='N':
        print('Finalizando...'),sleep(2)
        break
    if c == 9:
        print('Você excedeu o limite de cadastro! Finalizando...'),sleep(2)
print('-='*25)
print(f'{"No.":<4}{"NOME":<10}{"PREÇO":>8}')
print('-'*30)
for i,a in enumerate(lista):
    print(f'{i:<4}{a[0]:<15}R${a[1][0]:>8.2f}')
print('-'*15)
print(f'Total = R${total:.2f}')
print('-='*25)
print('''OPÇÕES DE PAGAMENTO:
[ 1 ] Á vista dinheiro/cheque (10% de desconto)
[ 2 ] Á vista Cartão débito (5% de desconto)
[ 3 ] 2x no Cartão 
[ 4 ] 3x ou mais no Cartão (20% de Juros)''')
opc=int(input('Qual a sua opção? '))
while opc > 4:
    print('Opção Inválida. Tente novamente!')
    opc = int(input('Qual a sua opção? '))
if opc==1:
    total1= total-(total*10/100)
elif opc==2:
    total1= total-(total*5/100)
elif opc==3:
    parcela= total/2
    total1=parcela
    print(f'Sua compra será parcela em 2x de R${parcela} SEM JUROS.')
elif opc==4:
    total1= total+(total*20/100)
    totparcela=int(input('Quantas parcelas? '))
    parcela= total/totparcela
    while totparcela > 12:
        print('Quantidade de parcelas inválida! Máximo é 12.')
        totparcela = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {totparcela}x de R${parcela:.2f} COM JUROS.')
    resp1 = ' '
    resp1=str(input('Confirmar pagamento? [S/N]')).strip().upper()[0]
    while resp1 not in 'SN':
        print('Dado Inválido. Tente Novamente!')
        resp1 = str(input('Confirmar pagamento? [S/N]')).strip().upper()[0]
    if resp1=='S':
        print('Realizando pagamento...'),sleep(2)
        print('Pagamento efetuado com sucesso!')
    elif resp1 == 'N':
        total1 = total
        print('Pagamento não realizado!')
        print('  <<< Volte Sempre! >>>')
        exit()
print(f'Sua compra deu no total R${total:.2f} e vai custar R${total1:.2f} no final.')
print(' <<< Volte Sempre! >>>')
