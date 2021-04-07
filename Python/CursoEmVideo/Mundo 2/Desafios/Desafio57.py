sexo=str(input('Qual o seu sexo: [M/F]')).strip().upper()[0]
while sexo !='M' and sexo!='F':
    sexo=str(input('Dado inválido. Por favor, informe seu sexo novamente:')).strip().upper()[0]
if sexo=='M' or sexo=='F':
    print(f'Sexo {sexo} cadastrado com sucesso.')
