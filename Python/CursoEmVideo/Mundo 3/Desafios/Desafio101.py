from datetime import date
ano_atual = date.today().year
def voto(ano):
    print('-='*15)
    idade = ano_atual-ano
    if idade <16:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif 16 >= idade < 18 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


anonasc= int(input('Ano de nascimento: '))
print(voto(anonasc))
