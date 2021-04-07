print('Vamos ver de quanto foi o aumento do salário!')
sal=float(input('Qual é o salário do funcionário? R$'))
if sal <=1250:
    novo= sal + (sal*15/100)
else:
    novo= sal+(sal*10/100)
print(f'Quem ganhava R${sal:.2f} passa a ganhar R${novo:.2f} agora.')
