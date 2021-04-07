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
