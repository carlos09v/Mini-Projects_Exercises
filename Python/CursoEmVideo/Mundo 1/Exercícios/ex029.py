km=float(input('Qual a velocidade atual do carro? '))
if km>80:
    print('MULTADO! Você excedeu o limite que é de 80Km/h')
    multa= (km-80)*7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia. Dirija com cuidado!')