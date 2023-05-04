from time import sleep

# 1.
    # print('Olá, mundo!')

# 2.
"""
    def showNumber(num: int):
        print(f'O número informado foi {num} !')
    showNumber(8)
"""

# 3.
def soma(num1: int, num2: int) -> str:
    return f'A soma de {num1} + {num2} = {num1 + num2}'
# print(soma(5, 8))

# 4.
    # nums = []
    # for c in range(4):
    #     num = float(input(f'Qual a sua {c+1} nota ? '))
    #     nums.append(num)
    # media = 0
    # for num in nums:
    #     media += num / len(nums)
    # print(f'A média é igual a {media:.2f}')

# 5.
def metrosPraCentimetros(num: float):
    print('Convertendo...'),sleep(2)
    return f'Convertendo {num} pra centímetros é igual a {num * 100} !'
# print(metrosPraCentimetros(3.12))

# 6.
    # Formula = A = π · r2
    # raio = int(input('Qual o raio do circulo? '))
    # print(f'A área é igual a {3.14 * (raio ** 2)} cm2')

# 7.
def areaQuadrado(comp, larg):
    print(f'O quadrado possui {comp * larg} metros ({comp}m x {larg}m)')
    print(f'O dobro da área é igual a {(comp * larg) * 2}')
# comprimento = int(input('Qual o comprimento do quadrado ? '))
# largura = int(input('Qual a largura ? '))
# areaQuadrado(comprimento, largura)

# 8.
    # ganhoHora = float(input('Quanto você ganha por hora ? '))
    # horasTrabalhadasMes = int(input('Quantas horas você trabalhou no mês ? '))
    # print(f'Seu salário será {ganhoHora * horasTrabalhadasMes:.0f}')

# 9.
    # Formula dada: (72.7*altura) - 58
    # alt = float(input('Qual a sua altura ? '))
    # print(f'Seu peso ideal é {(72.7 * alt) - 58:.0f}.')

# 10 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes formulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
def calcPesoIdeal():
    gen = str(input('Qual seu gênero Homem(H) ou Mulher(M) ? ')).strip().upper()[0]
    while gen not in 'HM':
        print('Dado inváldido. Tente novamente !')
        gen = str(input('Qual seu gênero Homem(H) ou Mulher(M) ? ')).strip().upper()[0]
    alt = float(input('Qual a sua altura? '))

    if gen == 'H':
        calc = (72.7 * alt) - 58
        return print(f'O peso ideal para Homem é {calc:.2f}')
    if gen == 'M':
        calc = (62.1 * alt) - 44.7
        return print(f'O peso ideal para Mulher é {calc:.2f}')
# calcPesoIdeal()

# 10.? - Faça um programa que receba um numero e informe se este eh primo
def isPrime(num):
    mult = 0

    for count in range(2, num):
        if (num % count == 0):
            mult += 1
    if (mult == 0):
        print(f'O número {num} é PRIMO !')
    else:
        print(f'Tem {mult} múltiplos acima de 2 e abaixo de {num}. Logo NÃO é primo !')
# isPrime(12)

# 10.? - Refaça a questao anterior para a qntidade de numeros que o usuario desejar (flag = -1)
def isPrime2(*nums):
    for num in nums:
        if (num == -1):
            print('Encerrado...')
            break

        mult = 0
        for count in range(2, num):
            if (num % count == 0):
                mult += 1
        if (mult == 0):
            print(f'O número {num} é PRIMO !')
        else:
            print(f'Tem {mult} múltiplos acima de 2 e abaixo de {num}. Logo NÃO é primo !')
# isPrime2(5, 8, 3, 12, 21, 32, 51, -1, 213)
