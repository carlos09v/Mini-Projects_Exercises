c = 0
while c < 10:
    c += 1
    print(c)
print('FIM!')

n = 1
while n != 0:
    n=int(input('Digite um valor:'))
print('FIM!')

r = 'S'
while r == 'S':
    n=int(input('Digite um valor:'))
    r=str(input('Quer continuar? [S/N]')).upper()
print('FIM!')

par = impar = 0
n = 1
while n != 0:
    n=int(input('Digite um número:'))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Você digitou {par} números PARES e {impar} números ÍMPARES.')
