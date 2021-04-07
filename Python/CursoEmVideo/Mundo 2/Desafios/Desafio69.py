sexoh = sexof = idade = 0
while True:
        idad1=int(input('Qual a sua idade?'))
        if idad1>18:
            idade += 1
        sexo1 = ' '
        while sexo1 not in 'MF':
            sexo1=str(input('Qual o seu sexo? [M/F]')).strip().upper()[0]
        if sexo1=='M':
            sexoh += 1
        if sexo1=='F' and idad1<20:
            sexof += 1
        print('Pessoa CADASTRADA com SUCESSO.')
        perg = ' '
        while perg not in 'SN':
            perg=str(input('Quer continuar a cadastrar? [S/N]')).strip().upper()[0]
        if perg=='N':
            break
print('---------- FIM DO PROGRAMA ----------')
print(f'Total de pessoas com mais de 18 anos: {idade}')
print(f'Ao todo temos {sexoh} homens cadastrados.')
print(f'E temos {sexof} mulheres com menos de 20 anos.')
