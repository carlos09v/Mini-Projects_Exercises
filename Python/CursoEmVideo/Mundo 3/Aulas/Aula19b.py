brasil = []
estado = dict()
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1])
print(brasil[0]['uf'])
brasil.clear()

for c in range(0,3):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['sigla']= str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}')
