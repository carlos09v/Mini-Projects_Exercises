lista=[]
count = 0
while True:
    l = int(input('Digite um valor:'))
    if l == 5:
        count += 1
    if l not in lista:
        lista.append(l)
        print(f'Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp=='N':
        break
    while resp not in 'S':
        print('Dado inválido! Tente novamente.')
        resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
print('-'*30)
print(f'Você digitou {len(lista)} números.')
print('='*20)
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
print('='*20)
if count>0:
    print(f'Você digitou o valor 5! {count} vezes')
else:
    print('Você não digitou o número 5.')
