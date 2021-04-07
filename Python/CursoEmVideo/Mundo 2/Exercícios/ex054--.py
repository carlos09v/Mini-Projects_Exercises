from datetime import date
atual=date.today().year
totamaior=0
totmenor=0
for pess in range(1,8):
    nasc=int(input(f'Em que ano a {pess} pessoa nasceu?'))
    idade= atual-nasc
    if idade>18:
        totamaior +=1
    elif idade < 18:
        totmenor += 1
print(f'No grupo, temos \033[34m{totamaior}\033[m pessoas maiores de idade.')
print(f'E \033[32m{totmenor}\033[m pessoas menores de idade.')
