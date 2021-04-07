#from math import factorial
#n1=int(input('Digite um número para calcular o seu Fatorial:'))
#f= factorial(n1)
#print(f'O fatorial de {n1} é {f}')

n1=int(input('Digite um número para calcular seu Fatorial:'))
c = n1
f = 1
print(f'Calculando {n1}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c>1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
