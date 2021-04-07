print('\033[4mRefazendo Desafio09:\033[m')
print('*\033[35mTabuada v.2.0\033[m*')
n=int(input('Vamos ver a tabudada do número:'))
for c in range(0,10+1):
    tab= n*c
    print(f'{n}*{c}= {tab}')
