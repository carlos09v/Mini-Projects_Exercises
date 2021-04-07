import random
print('Vamos ver qual vai ser a ordem de apresentação dos trabalhos.')
n1=str(input('Primeiro aluno:'))
n2=str(input('Segundo aluno:'))
n3=str(input('Terceiro aluno:'))
n4=str(input('Quarto aluino:'))
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print(f'A ordem de apresentação será:')
print(lista)