print('\033[32mEx:\033[m \033[33mFaça um programa que leia um número inteiro'
      ' e diga se ele é ou não um número primo.\033[m')
num=int(input('Digite um número:'))
tot=0
for c in range(1,num+1):
    if num%c==0:
        print('\033[34m',end='')
        tot+=1
    else:
        print('\033[31m',end='')
    print(c,end=' ')
print(f'\n\033[mO número \033[32m{num}\033[m foi divisível \033[33m{tot}\033[m vezes.')
if tot==2:
    print('E por isso ele é \033[34mPRIMO!\033[m')
else:
    print('E por isso ele \033[31mNÃO É PRIMO!\033[m')
