num = (int(input('Digite um número:')),
       int(input('Digite outro número:')),
       int(input('Digite mais um número:')),
       int(input('Digite o último número:')))
print(f'Você digitou os valores {num}')
print('='*20)
print(f'Apareceu {num.count(9)} vezes o valor 9.')
print('='*20)
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
print('='*20)
print('Os valores pares digitados foram: ',end='')
for c in num:
    if c % 2 == 0:
        print(c,end=' ')
