from random import randint
print('\033[36m-\033[m\033[32m#\033[m'*10)
print('\033[35mJogo do PAR ou ÍMPAR\033[m')
print('\033[36m-\033[m\033[32m#\033[m'*10)
count = 0
while True:
    jogador=str(input('\033[36mÍMPAR\033[m ou \033[32mPAR\033[m: [I/P]')).strip().upper()[0]
    pc = randint(0,10)
    if jogador!='I' and jogador!='Í' and jogador!='P':
        print('\033[31mEscolha Inválida. Tente novamente!\033[m')
    n=int(input('Digite o seu valor:'))
    soma= pc+n
    if jogador in 'IÍ':
        if soma % 2 == 1:
            print(f'O adversário colocou \033[33m{pc}\033[m e a soma deu \033[31m{soma}\033[m'
                  f'. O resultado é \033[36mÍMPAR\033[m.')
            print('\033[4:32m>>> Jogador Vence!\033[m')
            print('Vamos jogar novamente...')
        else:
            print(f'O adversário colocou \033[33m{pc}\033[m e a soma deu \033[31m{soma}\033[m'
                  f'. O resultado é \033[36mPAR\033[m.')
            print('\033[4:37m>>> Adversário Vence!\033[m')
            print('\033[31mGAME OVER!\033[m')
            break
    elif jogador=='P':
        if soma % 2 == 0:
            print(f'O adversário colocou \033[33m{pc}\033[m e a soma deu \033[31m{soma}\033[m'
                  f'. O resultado é \033[36mPAR\033[m.')
            print('\033[4:32m>>> Jogador Vence!\033[m')
            print('Vamos jogar novamente...')
        else:
            print(f'O adversário colocou \033[33m{pc}\033[m e a soma deu \033[31m{soma}\033[m'
                  f'. O resultado é \033[36mÍMPAR\033[m.')
            print('\033[4:37m>>> Adversário Vence!\033[m')
            print('\033[31mGAME OVER!\033[m')
            break
    count += 1
print(f'Você teve \033[33m{count}\033[m \033[34mVITÓRIAS CONSECUTIVAS\033[m!')
