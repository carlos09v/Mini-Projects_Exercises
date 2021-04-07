somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=''
totmulher20=0
print('\033[35m- Análise de Dados: -\033[m')
for c in range(1,5):
    print(f'\033[33m-----\033[m \033[36m{c}ª PESSOA\033[m \033[33m-----\033[m')
    nome=str(input('Nome:')).strip().title()
    idade=int(input('Idade:'))
    somaidade += idade
    sexo=str(input('Sexo [M/F]:')).strip().upper()
    if c==1 and sexo=='M':
        maioridadehomem=idade
        nomevelho=nome
    if sexo=='M' and idade>maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo=='F' and idade<20:
        totmulher20 += 1
mediaidade= somaidade/4
print(f'- A média de idade do grupo é de \033[34m{mediaidade}\033[m anos.')
print(f'- O homem mais velho tem \033[33m{maioridadehomem}\033[m anos e se chama \033[32m{nomevelho}\033[m.')
print(f'- Ao todo são \033[33m{totmulher20}\033[m mulheres com menos de 20 anos.')
