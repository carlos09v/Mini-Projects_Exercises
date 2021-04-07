from datetime import date
ano=int(input('Qual \033[1:32mano\033[m analisar?Coloque \033[1:33m0\033[m para analisar o ano atual: '))
if ano==0:
    ano=date.today().year
if ano%4 ==0 and ano%100 !=0 or ano%400 ==0:
    print(f'O ano \033[1:33m{ano}\033[m é \033[1:34mBISSEXTO.\033[m')
else:
    print(f'O ano \033[1:33m{ano}\033[m \033[1:31mNÃO\033[m é \033[1:34mBISSEXTO.\033[m')