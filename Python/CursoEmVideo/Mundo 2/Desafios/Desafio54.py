from datetime import date
atual=date.today().year
count=0
count1=0
for c in range(1,8):
    ano=int(input(f'Em que ano a {c}ª pessoa nasceu?:'))
    if atual-ano <21:
        count += 1
    elif atual-ano >= 21:
        count1 += 1
print(f'Ao todo tivemos \033[32m{count}\033[m pessoas menores de idade.')
print(f'E também tivemos \033[34m{count1}\033[m pessoas maiores de idade.')
