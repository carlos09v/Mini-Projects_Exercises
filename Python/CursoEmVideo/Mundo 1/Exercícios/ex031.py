km=float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a iniciar uma viagem de {km:.0f}Km')
preço= km*0.50 if km <=200 else km*0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')