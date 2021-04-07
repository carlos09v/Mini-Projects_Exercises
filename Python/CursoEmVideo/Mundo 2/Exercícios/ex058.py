from random import randint
print('\033[32mEx:\033[m \033[4mRefazer o desafio28\033[m')
print('\033[37m-=-\033[m'*8)
print('\033[31mJoga da Adivinhação v2.0\033[m')
print('\033[37m-=-\033[m'*8)
print('Vou pensar em um número de \033[4:36m0 a 10\033[m. Tente adivinhar!')
pc=randint(0,10)
acertou= False
palpites = 0
while not acertou:
    jogador=int(input('Qual é o seu palpite?'))
    palpites += 1
    if jogador==pc:
        acertou= True
    else:
        if jogador<pc:
            print('Mais...')
        elif jogador>pc:
            print('Menos...')
print('\033[34mAcertou!\033[m')
print(f'Você acertou com \033[33m{palpites}\033[m tentativas.')
