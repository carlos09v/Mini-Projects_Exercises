# OBS: Fiz sozinho - Carlos Vinicius

from time import sleep
from random import randint, choice
from datetime import datetime

# Imprime o Menu
def menu():
    print('''\n========================= MENU =========================
  1 - Cadastrar Aluno
  2 - Alterar Aluno
  3 - Buscar Aluno por matrícula
  4 - Relatórios
  5 - Configurações
  6 - Sair
  ''')

    opc = int(input('Qual a opção? '))
    while opc < 1 or opc > 6:
        print('Opção Inválida ! Digite um número entre 1 e 6 :)')
        opc = int(input('Qual a opção? '))
    return opc


# Criar/Gerar Configuração
def registerConfig(studentName: str = '', studentMatricula: str = ''):
    cursoName = ''
    professores = ['Diego Aguiar', 'Juliette', 'Tarcício do Acordeão', 'Michel Teló', 'Ivete Sangalo']
    grades = {
        'Gastronomia': ['Cozinha Nutricional', 'Excelência em Serviços de Alimentos e Bebidas',
                        'Antropologia e História da Alimentação'],
        'Direito': ['Introdução ao Direito', 'Direito Romano', 'Direito Civil', 'Direito Constitucional'],
        'Medicina': ['Anatomia', 'Biologia celular', 'Farmacologia', 'Imunologia', 'Fisiologia', 'Patologia'],
        'TI - Tecnologia da Informação': ['INTRODUÇÃO À PROGRAMAÇÃO ESTRUTURADA EM C',
                                          'INTRODUÇÃO À SEGURANÇA DA INFORMAÇÃO', 'BANCO DE DADOS',
                                          'DESENVOLVIMENTO RÁPIDO DE APLICAÇÕES EM PYTHON', 'ENGENHARIA DE SOFTWARE',
                                          'SISTEMAS OPERACIONAIS'],
        'Administração': ['MATEMÁTICA EMPRESARIAL', 'PRINCÍPIOS DE GESTÃO', 'CONTABILIDADE GERAL',
                          'MATEMÁTICA FINANCEIRA']
    }

    print('\n\t<< Cadastrando dados do Curso:')
    print('Qual CURSO você quer seguir ?')
    for index, g in enumerate(grades.keys()):
        print(f'\t{index + 1} - {g}')

    opcGrad = int(input('Escolha uma opção [1 a 5]: '))
    while opcGrad < 1 or opcGrad > 5:
        print('Número Inválido! Digite um valor de 1 a 5.')
        opcGrad = int(input('Escolha uma opção [1 a 5]: '))
    match (opcGrad):
        case 1:
            cursoName = 'Gastronomia'
        case 2:
            cursoName = 'Direito'
        case 3:
            cursoName = 'Medicina'
        case 4:
            cursoName = 'TI - Tecnologia da Informação'
        case 5:
            cursoName = 'Administração'
    print(f'\n<< Curso [ {cursoName} ]')
    print('\tDisciplinas disponíveis:')
    for index, value in enumerate(grades[cursoName]):
        print(f'\t{index + 1} - ( {value} )')
    opcDiscip = int(input(f'Escolha uma opção [1 a {len(grades[cursoName])}]: '))
    while opcDiscip < 1 or opcDiscip > len(grades[cursoName]):
        print(f'Número Inválido! Digite um valor de 1 a {len(grades[cursoName])}.')
        opcDiscip = int(input(f'Escolha uma opção [1 a {len(grades[cursoName])}]: '))

    randomProfessor = choice(professores) # Get a random value from array
    print('\n- Professor escolhido (disponivel): ' + randomProfessor)
    with open('config.txt', 'a', encoding='UTF-8') as config:
        config.write('= Configurações ================================\n')
        config.write(f'\t- Aluno: {studentName}\n')
        config.write(f'\t- Matricula: {studentMatricula}\n')
        config.write(f'\t\t< Curso escolhido: {cursoName}\n')
        config.write(f'\t\t< Disciplina: {grades.get(cursoName)[opcDiscip - 1]}\n')
        config.write(f'\t\t< Professor: {randomProfessor}\n')
    print('Dados salvos no banco com sucesso :)'), sleep(2)
    main()

# Criar/Cadastrar Aluno
def registerStudent():
    notas = []

    print('--------- Cadastro de Aluno(a) ---------')
    nome = str(input('Qual o nome?'))
    # matricula = randint(10000000, 100000000) # De qnto ate qnto => random
    matricula = datetime.now().strftime('%Y%m%d%H%M%S')  # Date and Time Format: %d/%m/%Y %H:%M:%S
    for n in range(3):
        nota = float(input(f'Qual a sua {n + 1}° nota: '))
        notas.append(nota)
    qntdade_faltas = int(input('Quantos dias você faltou? '))
    media = sum(notas) / len(notas)

    formatedName = nome.title().strip()
    with open('alunos.txt', 'a') as register:
        register.write('= Cadastro ================================\n')
        register.write(f'\t- Nome: {formatedName}\n')
        register.write(f'\t- Matricula: {matricula}\n')
        register.write(f'\t- Notas: {notas}\n')
        register.write(f'\t- Quantidade de Faltas: {qntdade_faltas}\n')
        register.write(f'\t- Media: {media:.1f}\n')
    print('Dados salvos no banco com sucesso :)'), sleep(2)
    registerConfig(formatedName, matricula)

# Encontrar aluno pela Matricula
def findStudent(matricula: str):
    with open('alunos.txt', 'r') as aluno:
        lines = aluno.readlines()
        for index, line in enumerate(lines):
            if matricula in line:
                print(f'\n< Matricula {matricula} encontrada!')
                print(lines[index-1])
                print(lines[index])
                print(lines[index+1])
                print(lines[index+2])
                print(lines[index+3])
                break
    with open('config.txt', 'r', encoding='UTF-8') as config:
        lines = config.readlines()
        for index, line in enumerate(lines):
            if matricula in line:
                print(lines[index + 1])
                print(lines[index + 2])
                print(lines[index + 3]), sleep(3)
                break

def main():
    opc = menu()

    match (opc):
        case 1:
            registerStudent()
        case 2:
            print('Alert: Ainda em desenvolvimento ...'), sleep(2)
            main()
        case 3:
            try:
                open('alunos.txt', 'r')
                open('config.txt', 'r')

                matricula = str(input('Qual a matricula do aluno? '))
                while not len(matricula) == 14:
                    print('Erro: A matricula precisa ter 14 numeros !')
                    matricula = str(input('Qual a matricula do aluno? '))
                findStudent(matricula)
                if not findStudent:
                    print('Matricula não econtrada :('), sleep(3) # Bug

                main()
            except FileNotFoundError:
                print('Erro: Arquivo inexistente! Cadastre o primeiro aluno ...')
                main()
        case 4:
            print('''
4.1 - Listar todos os alunos
4.2 - Listar alunos aprovados (Critério de aprovação média >= 6,0 e frequência >= 75%)
4.3 - Listar alunos reprovados por faltas (frequência < 75%)
4.4 - Listar dados completos do aluno de maior média
4.5 - Listar dados completos do aluno de menor média
                ''')
            print('Alert: Ainda em desenvolvimento ...'), sleep(2)
            main()
        case 5:
            try:
                with open('config.txt', 'r', encoding='UTF-8') as config:
                    # não é necessário fechar o arquivo apos utilização.
                    print(config.read()), sleep(3)
                    main()
            except FileNotFoundError as Erro1:
                # print(Erro1)
                print('Erro: Arquivo inexistente! Cadastre o primeiro aluno para as Configurações serem geradas...'), sleep(2)
                main()
            except PermissionError:
                print('Você não tem permissão para alterar esse arquivo :(')
                print(PermissionError)
                main()
        case 6:
            print('Finalizando...'), sleep(3)


main()
