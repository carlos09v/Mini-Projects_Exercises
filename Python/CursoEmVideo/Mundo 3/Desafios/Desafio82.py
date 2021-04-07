lista=[]
while True:
    l = int(input('Digite um valor:'))
    if l not in lista:
        lista.append(l)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp=='N':
        break
    while resp not in 'S':
        print('Dado inválido! Tente novamente.')
        resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
listapar=[]
listaimpar=[]
for n in range(0,len(lista)):
    if lista[n] % 2 == 0:
        listapar.append(lista[n])
    else:
        listaimpar.append(lista[n])
print('-='*30)
print(f'Lista com todos os números: {lista}')
print(f'Lista com números pares: {listapar}')
print(f'Lista com números ímpares: {listaimpar}')
