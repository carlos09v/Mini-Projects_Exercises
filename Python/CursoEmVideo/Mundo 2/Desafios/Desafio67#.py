print('\033[33m=\033[m\033[31mX\033[m'*10)
print('\033[35m    TABUADA v3.0\033[m')
print('\033[33m=\033[m\033[31mX\033[m'*10)
while True:
    tab=int(input('Digite um número pra ver sua tabuada:'))
    print('-'*30)
    if tab<0:
        break
    for c in range(0,11):
        print(f'{tab} x {c} = {tab*c}')
    print('-'*30)
    print('Use um número \033[37mnegativo\033[m para \033[31mPARAR\033[m!')
print('Programa \033[31mTABUADA ENCERRADO\033[m. Volte sempre!')
