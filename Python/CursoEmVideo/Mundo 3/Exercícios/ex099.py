from time import sleep
def maior(* num):
    cont = maior = 0
    print('-='*20)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ',end=''),sleep(0.3)
        cont += 1
    print(f'| Foram informados {cont} valores ao todo.')
    print(f'O maior valor passado é {max(num)}.')


# Programa principal
maior(2,9,4,3,5,10)
maior(5,6)
maior(3)
