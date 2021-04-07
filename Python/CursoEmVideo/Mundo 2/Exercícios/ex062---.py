print('\033[35mGerador de PA v3.0\033[m')
print('\033[31m-=\033[m'*10)
prim=int(input('Digite o primerio termo:'))
raz=int(input('Digite a razão:'))
termo = prim
count = 1
total = 0
mais = 10
while mais!=0:
    total= total+mais
    while count <=total:
        print(f'{termo} - ', end='')
        termo += raz
        count += 1
    print('PAUSA')
    mais=int(input('Quantos termos você quer mostrar mais?'))
print('FIM!')
print(f'Progressão finalizada com \033[33m{total}\033[m termos mostrados.')
