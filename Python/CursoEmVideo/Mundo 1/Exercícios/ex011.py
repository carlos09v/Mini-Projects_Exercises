print('Vamos calcular a área e quantidade de tinta necessária pra pintar uma parede!')
larg=float(input('Largura da parede:'))
alt=float(input('Altura da parede:'))
a=alt*larg
print(f'Sua parede tem dimensão de {larg}*{alt} e sua área é de {a:.2f}m2.')
tinta=a/2
print(f'Para pintar essa parede, você precisará de {tinta:.1f}l de tinta.')
