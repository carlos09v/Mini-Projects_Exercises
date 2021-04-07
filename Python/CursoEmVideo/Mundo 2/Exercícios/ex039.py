from datetime import date
print('\033[35m-\033[m'*30)
print('\033[36mAlistamento Militar para Homens\033[m')
print('\033[35m-\033[m'*30)
atual=date.today().year
nasc=int(input('Ano de nascimento?'))
idade=atual-nasc
print(f'Quem nasceu em \033[33m{nasc}\033[m tem \033[34m{idade}\033[m anos em \033[33m{atual}\033[m.')
if idade==18:
    print('Você tem que se alistar \033[32mIMEDIATAMENTE\033[m!')
elif idade<18:
    saldo=18-idade
    print(f'Você ainda não tem \033[34m18 anos\033[m. Ainda faltam \033[32m{saldo}\033[m anos para o alistamento.')
    ano=atual+saldo
    print(f'Seu alistamento será em \033[33m{ano}\033[m.')
elif idade>18:
    saldo=idade-18
    print(f'Você já deveria ter se alistado há \033[32m{saldo}\033[m anos.')
    ano=atual-saldo
    print(f'Seu alistamento foi em \033[33m{ano}\033[m.')
