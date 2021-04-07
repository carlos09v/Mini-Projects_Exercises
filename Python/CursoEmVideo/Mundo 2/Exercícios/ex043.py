peso=float(input('Qual é o seu peso? (Kg)'))
altura=float(input('Qual a sua altura? (m)'))
imc=peso/(altura**2)
print(f'Seu IMC é de {imc:.1f}')
if imc<18.5:
    print('Você está ABAIXO DO PESO normal!')
elif 18.5<=imc<25:
    print('Você está na faixa de PESO NORMAL!')
elif 25<=imc<30:
    print('Você está na faixa SOBREPESO!')
elif 30<=imc<40:
    print('Você está na faixa OBESIDADE!')
elif imc>=40:
    print('Você está na faixa OBESIDADE MÓRBIDA , cuidado!')
