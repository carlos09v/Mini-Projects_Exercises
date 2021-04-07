#Retorno de valores
def somar(a=0,b=0,c=0):
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)
print(f'Meus cálculos dera {r1} , {r2} , {r3}.')

def fatorial(num=1):
    f = 1
    for c in range(num, 0 ,-1):
        f *= c
    return f
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1} , {f2} , {f3}.')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('É PAR!')
else:
    print('É ÍMPAR!')
