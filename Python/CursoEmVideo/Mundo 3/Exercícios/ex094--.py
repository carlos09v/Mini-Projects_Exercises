galera = list()
pessooa = dict()
soma = media = 0
print(f'{"== Análise de Dados ==":^20}')
while True:
    pessooa.clear()
    pessooa["nome"] = str(input('Nome: ')).title()
    while True:
        pessooa["sexo"]=str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessooa["sexo"] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessooa["idade"]=int(input('Idade: '))
    soma += pessooa["idade"]
    galera.append(pessooa.copy())
    while True:
        resp=str(input('Quer continar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apena S ou N.')
    if resp=='N':
        break
print('-='*30)
media = soma/len(galera)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram | ',end='')
for p in galera:
    if p["sexo"]=='F':
        print(f'{p["nome"]} | ',end='')
print()
print(f'D) Lista de pessoas que estão acima da média:')
for p in galera:
    if p["idade"]>=media:
        print('    ',end='')
        for k,v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print(' << ENCERRADO >>')
