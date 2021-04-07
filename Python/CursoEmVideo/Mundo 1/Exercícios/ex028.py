from random import randint
from time import sleep
pc= randint(0,5) #Faz o pc "PENSAR"
print('\033[35m-=-\033[m'*20)
print('Vamos jogar o \033[1:34mJogo da Adivinhação!\033[m')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[35m-=-\033[m'*20)

player=(int(input('Em que número eu pensei? '))) # Player tenta adivinhar
print('\033[1:31mPROCESSANDO...\033[m')
sleep(3)
if player==pc:
    print('\033[1:33mParabéns.\033[m Você conseguiu me vencer!')
else:
    print(f'\033[1:31mGanhei!\033[m Eu pensei no número \033[1:35m{pc}\033[m e \033[1mnão\033[m no \033[1:33m{player}'
          f'\033[m.')
