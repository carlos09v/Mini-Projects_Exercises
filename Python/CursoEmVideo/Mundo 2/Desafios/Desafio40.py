nota1=float(input('Qual foi a sua primeira nota:'))
nota2=float(input('Qual foi a segunda nota:'))
media=(nota1+nota2)/2
if media <5:
    print(f'Sua média é \033[34m{media}\033[m. Sinto muito,você está \033[31mREPROVADO\033[m!')
elif media >=5 and media <=6.9:
    print(f'Sua média é \033[34m{media}\033[m. Logo,você está de \033[33mRECUPERAÇÃO\033[m.')
else:
    print(f'Sua média é \033[34m{media}\033[m. Você está \033[32mAPROVADO\033[m. Parabéns!')
