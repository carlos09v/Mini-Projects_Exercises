dados = dict()
dados['nome']=str(input('Nome: '))
dados['media']=float(input('Média: '))
print(f'Nome é igual a {dados["nome"].title()}')
print(f'Média é igual a {dados["media"]}')
print(f'Situção é igual a ',end='')
if dados['media']>=7:
    print('Aprovado!')
elif dados['media']<7 and dados['media']>=6:
    print('Recuperação!')
else:
    print('Reprovado!')
