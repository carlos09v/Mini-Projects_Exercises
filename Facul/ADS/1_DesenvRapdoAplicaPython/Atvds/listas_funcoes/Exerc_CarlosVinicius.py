# Obs: Fiz sozinho ! - Carlos Vinicius

# 15 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
def showInverse():
    array = []
    for c in range(10):
        num = int(input(f'{c + 1} número: '))
        array.append(num)
    array.reverse()  # -> Reverse Function
    for c in array:
        print(c)
# showInverse()

# 16 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
def calcMedia():
    notas = []
    for c in range(4):
        nota = float(input(f'{c + 1} nota: '))
        notas.append(nota)
    media = sum(notas) / len(notas)  # -> Sum + Length Functions
    for n in range(len(notas)):
        print(f'{n + 1} nota: {notas[n]}')
    print(f'A média é {media:.2f}')
# calcMedia()

# 17 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números PARES no vetor par e os números ÍMPARES no vetor impar. Imprimar o três vetores.
def paresEimpares():
    todos = []
    pares = []
    impares = []
    for n in range(20):
        num = int(input(f'{n + 1} número: '))
        todos.append(num)
        if (num % 2 == 0):
            pares.append(num)
        if (num % 2 == 1):
            impares.append(num)
    print(f'Todos os números: {todos}')
    print(f'Números pares: {pares}')
    print(f'Números ímpares: {impares}')
# paresEimpares()

# 18 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.
def mediaMaiorQue7():
    medias = []
    qntd_alunos = 0
    for n in range(10):
        soma = 0
        print(f'Notas do {n+1} aluno: ')
        for c in range(4):
            nota = float(input(f'Qual a {c+1} nota? '))
            soma += nota
        media = soma / 4
        if media > 7:
            qntd_alunos += 1
        medias.append(media)
    print(f'{qntd_alunos} aluno(s) teve a média maior que 7.')
    print(medias)
# mediaMaiorQue7()

# 19 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
def somaEMutiplica():
    nums = []
    soma = 0

    print('Digite 5 números inteiros.')
    for c in range(5):
        num = int(input(f'{c+1} número: '))
        soma += num
        nums.append(num)
    mult = soma * 2
    print(f'Os números são {nums}')
    print(f'A soma dos números é {soma}')
    print(f'A multiplicação é {mult}')
# somaEMutiplica()

# 20 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
def idadeEAlturaReverse():
    idades = []
    alturas = []

    print('Informe a Idade e Altura de 5 pessoas.')
    for p in range(5):
        print(f'{p+1} pessoa:')
        idad = int(input('Qual a sua idade? '))
        alt = float(input('Sua altura? '))
        idades.append(idad)
        alturas.append(alt)
    idades.reverse()
    alturas.reverse()
    print(f'Idades Inversas: {idades}')
    print(f'Alturas Inversas: {alturas}')
# idadeEAlturaReverse()

# 21 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
def somaQuadrados():
    a = []

    print('Informe 10 números Inteiros: ')
    for c in range(10):
        num = int(input(f'{c+1} número: '))
        a.append(num)
    somaAoQuadrado = sum(a) ** 2
    print(f'A soma dos quadrados é {somaAoQuadrado}')
# somaQuadrados()

# 22 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
def valoresIntercalados():
    a = []
    b = []

    print('Informe 10 valores pro primeiro vetor: ')
    for c in range(10):
        num = float(input(f'{c+1} valor: '))
        a.append(num)
    print('Informe 10 valores pro segundo vetor: ')
    for c in range(10):
        num = float(input(f'{c+1} valor: '))
        b.append(num)

    c = a + b
    c[::2] = a
    c[1::2] = b
    print(f'O números Intercalados são: {c}')
# valoresIntercalados()

# 23 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
def quizAboutCrimes():
    quests = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]

    respostas = []
    classificacao = ['Suspeita', 'Cúmplice', 'Assassino', 'Inocente']
    for q in quests:
        resp = str(input(q)).upper().strip()[0]
        respostas.append(resp)
    if respostas.count('S') == 2:
        classificacao = classificacao[0]
    elif 5 > respostas.count('S') > 2:
        classificacao = classificacao[1]
    elif respostas.count('S') == 5:
        classificacao = classificacao[2]
    else:
        classificacao = classificacao[3]
    print(respostas)
    print(f'Sua categoria é: {classificacao}')
# quizAboutCrimes()

# Funções --
# 24 - Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def soma(num1, num2, num3):
    return f'A soma do três valores é: {num1 + num2 + num3}'
print(soma(3, 6, 12))

# 25 - Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def checkPositive(num):
    if num > 0:
        return 'P'
    else:
        return 'N'
print(checkPositive(5))
print(checkPositive(-65))
print(checkPositive(0))