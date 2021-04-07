km=float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a iniciar uma viagem de {km:.0f}Km')
if km <=200:
    preço=km*0.50
else:
    preço=km*0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')
