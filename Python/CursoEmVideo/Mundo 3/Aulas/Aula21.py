# Interactive Help
help(print)
print(input.__doc__)

# Docstrings
def contador(i,f,p):
    ''' #docstrings
        > Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Oláaaaa!
    '''
    c = i
    while c<=f:
        print(f'{c} ',end='')
        c += p
    print('FIM!')
help(contador)

# Parâmetros Opcionais
def somar(a=0,b=0,c=0):
    s = a + b + c
    print(f'A soma vale {s}.')
somar(8,6,9)
somar(8,6)
somar()
somar(b=6,a=2)

# Escopo de Variáveis
def teste():
    #global n
    n = 5 #Variável local
    print(f'A função de n é {n}.')

n = 3 #Variável global
print(f'O programa de n é {n}')
teste()
