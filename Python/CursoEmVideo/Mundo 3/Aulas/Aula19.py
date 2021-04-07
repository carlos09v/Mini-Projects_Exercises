bio = {'nome':'Carlos V.','idade':17,'sexo':'M',
       'sobre':'Me torno adulto amnha, dezoitooou!!'}
print(f'O {bio["nome"]} tem {bio["idade"]} anos.')
print(bio.keys())
print(bio.values())
print(bio.items())

del bio["sexo"]
bio["nome"] = 'SoNoDally'
bio["peso"] = 70
for k in bio.keys():
    print(k)
for k,v in bio.items():
    print(f'{k} = {v}')
