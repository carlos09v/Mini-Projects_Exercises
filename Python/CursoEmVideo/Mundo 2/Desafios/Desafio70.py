print('======== Análise de Produtos ======== ')
soma = preço1000 = menor = cont = 0
nomeprod = ''
while True:
        nome=str(input('Qual o nome do produto?'))
        preço=float(input('Qual o preço do produto? R$'))
        soma += preço
        cont += 1
        if cont == 1 or preço < menor:
            menor = preço
            nomeprod = nome
        if preço>1000:
            preço1000 += 1
        print('Produto CADASTRADO com SUCESSO.')
        perg = ' '
        while perg not in 'SN':
            perg = str(input('Quer continuar o cadastro? [S/N]')).strip().upper()[0]
        if perg=='N':
            break
print('========== FIM DO PROGRAMA ===========')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {preço1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeprod} e custa R${menor:.2f}')
