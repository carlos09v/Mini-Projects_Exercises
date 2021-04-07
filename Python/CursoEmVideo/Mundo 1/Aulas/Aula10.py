nome=str(input('Qual o seu nome: '))
if nome=='Carlos':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão comum!')
print(f'Bom dia, {nome.title()}!')

print('Vamos ver a sua média.')
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m= (n1+n2)/2
print(f'A sua média foi {m:.1f}')
if m >=6.0:
    print('Logo,você ficou acima da média. Parabéns!')
else:
    print('Você ficou abaixou da média. Estude mais da próxima vez!')
