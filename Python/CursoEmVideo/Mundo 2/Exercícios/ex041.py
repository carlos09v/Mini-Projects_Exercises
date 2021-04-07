from datetime import date
atual=date.today().year
print('\033[35m*\033[m'*30)
print('\033[34mConfederação Nacional de Natação\033[m')
print('\033[35m*\033[m'*30)
print('''Categoria dos Atletas:
| até 9 anos: \033[36mMIRIM\033[m |
| até 14 anos: \033[34mINFANTIL\033[m |
| até 19 anos: \033[32mJUNIOR\033[m |
| até 25 anos: \033[35mSÊNIOR\033[m |
| Mais de 25 anos: \033[37mMASTER\033[m |''')
nasc=int(input('Ano de Nascimento:'))
idade=atual-nasc
print('Classificação do Atleta:')
print(f'O atleta tem \033[33m{idade}\033[m anos.')
if idade<=9:
    print('O atleta está na categoria: \033[36mMIRIM\033[m')
elif idade<=14:
    print('O atleta está na categoria: \033[34mINFANTIL\033[m')
elif idade<=19:
    print('O atleta está na categoria: \033[32mJUNIOR\033[m')
elif idade<=25:
    print('O atleta está na categoria: \033[35mSÊNIOR\033[m')
else:
    print('O atleta está na categoria: \033[37mMASTER\033[m')
