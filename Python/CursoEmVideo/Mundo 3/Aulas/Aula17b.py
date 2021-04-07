lista= []
lista.append(8)
lista.append(10)
lista.append(21)

for cont in range(0,3):
    lista.append(int(input('Digite um valor:')))

for c,v in enumerate(lista):
    print(f'Na {c+1}ª posição encontrei o valor {v}!')
print('Cheguei ao final da lista.')

listaA = [3,5,4,6]
listaB = listaA[:] #Cópia
#listaB = listaA (Repete)
listaB[1] = 2
print(f'Lista A: {listaA}')
print(f'Lista B: {listaB}')
