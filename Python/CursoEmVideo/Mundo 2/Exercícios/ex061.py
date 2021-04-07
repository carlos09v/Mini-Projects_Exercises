print('\033[31mGerador de PA v2.0\033[m')
print('\033[33m-=\033[m'*10)
prim=int(input('Digite o primerio termo:'))
raz=int(input('Digite a razão:'))
termo = prim
cont = 1
while cont <= 10:
    print(f'{termo} - ', end='')
    termo += raz
    cont += 1
print('FIM!')
