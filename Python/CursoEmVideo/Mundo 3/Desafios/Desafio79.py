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
    if resp!='S':
        print('Dado inválido! Tente novamente.')
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp=='N':
        break
print('-='*30)
lista.sort()
print(f'Você digitou os valores: {lista}')
