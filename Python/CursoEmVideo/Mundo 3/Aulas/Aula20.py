def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
def contador(* num):  #Tupla  #Desempacotar
    for valor in num:
        print(f'{valor} ',end='')
    print('Fim!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
def dobra(lst):  #Lista
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
# Programa Principal
soma(3,4)
soma(a=8,b=9)
soma(b=2,a=1)
print()
contador(2,6,9,4)
contador(2,9,3)
contador(3)
print()
valores = [6,5,3,8,9,10]
dobra(valores)
print(valores)
