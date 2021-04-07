from random import randint
from time import sleep
print('$='*15)
print(f'{"Jogue na Mega Cena":^30}')
print('$='*15)
n=int(input('Quantos jogos você quer que eu sorteie: '))
print(f'-=-=-= SORTEANDO {n} JOGOS -=-=-=')
for p in range(n):
    lista = [randint(0, 60), randint(0, 60), randint(0, 60),
             randint(0, 60), randint(0, 60), randint(0, 60)]
    lista.sort()
    print(f'Jogo {p+1}: {lista}'),sleep(1)
print('-='*4,end='')
print(' < BOA SORTE! > ',end='')
print('-='*4)
