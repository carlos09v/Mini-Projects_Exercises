valores = []
while True:
    valores.append(int(input('Digite um valor:')))
    resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp=='N':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos.')
print('-='*30)
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
print('-='*30)
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
