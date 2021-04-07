from datetime import datetime
print(f'{" == Cadastro de Trabalhador ==":^20}')
dados = dict()
dados["nome"]=str(input('Nome: ')).title()
nasc = int(input('Ano de nascimento: '))
dados["idade"]= datetime.now().year - nasc
dados["ctps"]=int(input('Carteira de Trabalho (0 não tem): '))
if dados["ctps"]!=0:
    dados["contratação"]=int(input('Ano de Contratação: '))
    dados["salário"]=float(input('Salário: R$'))
    dados["aposentadoria"]= dados["idade"] + ((dados["contratação"]+35) - datetime.now().year)
print('-='*30)
for c,v in dados.items():
    print(f'  - {c} é igual a {v}.')
