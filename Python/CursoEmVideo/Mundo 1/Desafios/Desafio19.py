print('Sorteio entre quem vai apagar o quadro!')
import random
alu1=(input('Nome do primeiro aluno:'))
alu2=(input('Nome do segundo aluno:'))
alu3=(input('Nome do terceiro aluno:'))
alu4=(input('Nome do ultimo aluno:'))
lista=[alu1,alu2,alu3,alu4]
a=random.choice(lista)
print(f'O aluno sorteado é {a}.')