from random import randint
from time import sleep
numeros = list()
def sorteia():
    print('-='*20)
    print('Sorteando 5 valores...')
    for c in range(0,5):
        n = randint(1,999)
        numeros.append(n)
        print(f'{n} ',end=''),sleep(0.3)
def somaPar():
    numerossum = sum(numeros)
    print(f'| A soma dos valores sorteados é {numerossum}.')


sorteia()
somaPar()
