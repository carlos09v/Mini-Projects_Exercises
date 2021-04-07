def metade(num=0,formato=False):
    res = num / 2
    return res if formato is False else moeda(res)

def dobro(num=0,formato=False):
    res = num * 2
    return res if formato is False else moeda(res)

def aumentar(num=0,porc=0,formato=False):
    res = num+(num*porc/100)
    return res if not formato else moeda(res)

def diminuir(num=0,porc=0,formato=False):
    res = num-(num*porc/100)
    return res if not formato else moeda(res)

def moeda(num=0,moeda='R$'):
    res = f'{moeda}{num:.2f}'.replace('.',',')
    return res

def resumo(num=0,aumen=10,dimin=5):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado: \t\t{moeda(num)}') #\t - tabulação
    print(f'O dobro do preço: \t\t{dobro(num,True)}')
    print(f'Metade do preço: \t\t{metade(num,True)}')
    print(f'Com {aumen}% de aumento: \t{aumentar(num,aumen,True)}')
    print(f'Com {dimin}% de redução: \t{diminuir(num,dimin,True)}')
    print('-'*30)
