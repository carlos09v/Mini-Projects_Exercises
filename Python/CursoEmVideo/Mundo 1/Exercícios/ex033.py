a=int(input('Primeiro Valor: '))
b=int(input('Segundo Valor: '))
c=int(input('Terceiro Valor: '))
# Verificando quem é o menor
menor= a
if b<c and b<a:
    menor= b
if c<a and c<b:
    menor= c
# Verificando quem é o maior
maior= a
if b>c and b>a:
    maior= b
if c>a and c>b:
    maior= c
print(f'O menor Valor é {menor}')
print(f'O maior Valor é {maior}')

