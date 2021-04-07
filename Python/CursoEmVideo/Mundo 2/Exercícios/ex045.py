from random import randint
from time import sleep
print(f'\033[31m{":"::^20}\033[m')
print('\033[36mVamos jogar Jokenpo!\033[m')
print(f'\033[31m{":"::^20}\033[m')
itens= ('Pedra','Papel','Tesoura')
pc= randint(0,2)
print('''\033[37mSuas opções:\033[m
\033[33m[\033[m \033[32m0\033[m \033[33m]\033[m PEDRA
\033[33m[\033[m \033[32m1\033[m \033[33m]\033[m PAPEL
\033[33m[\033[m \033[32m2\033[m \033[33m]\033[m TESOURA''')
player=int(input('\033[35mQual é a sua jogada?\033[m'))
print('\033[31mJO\033[m')
sleep(1)
print('\033[31mKEN\033[m')
sleep(1)
print('\033[31mPO!\033[m')

print('\033[33m-=\033[m'*10)
print(f'\033[4:35mComputador\033[m jogou {(itens[pc])}')
print(f'\033[4:32mJogador\033[m jogou {(itens[player])}')
print('\033[33m-=\033[m'*10)
if pc==0: #Pedra
    if player==0:
        print('\033[33m|EMPATE|\033[m')
    elif player==1:
        print('\033[32m|JOGADOR VENCE|\033[m')
    elif player==2:
        print('\033[35m|COMPUTADOR VENCE|\033[m')
    else:
        print('\033[37mJOGADA INVÁLIDA!\033[m')
elif pc==1: #Papel
    if player == 0:
        print('\033[35m|COMPUTADOR VENCE|\033[m')
    elif player == 1:
        print('\033[33m|EMPATE|\033[m')
    elif player == 2:
        print('\033[32m|JOGADOR VENCE|\033[m')
    else:
        print('\033[37mJOGADA INVÁLIDA!\033[m')
elif pc==2: #Tesoura
    if player == 0:
        print('\033[35m|JOGADOR VENCE|\033[m')
    elif player == 1:
        print('\033[32m|COMPUTADOR VENCE|\033[m')
    elif player == 2:
        print('\033[33m|EMPATE|\033[m')
    else:
        print('\033[37mJOGADA INVÁLIDA!\033[m')
