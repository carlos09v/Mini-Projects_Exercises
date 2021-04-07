print('\033[32mEx:\033[m \033[35mDesenvolva um programa que leia o primeiro termo e a razão de uma PA.'
      ' No final, mostre os 10 primeiros termos dessa progressão.\033[m')
primeiro=int(input('Primeiro termo:'))
razão=int(input('Razão:'))
décimo= primeiro+(10-1)*razão
for c in range(primeiro,décimo+razão,razão):
    print(c,end=' - ')
print('Acabou!')
