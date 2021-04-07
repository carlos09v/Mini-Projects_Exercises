lanche = 'Hambúrguer','Batata Frita','Peixe','Macarrão'
print(lanche[-2])

print(lanche[3])

print(lanche[2:])

print(lanche[:3])

#Tuplas são Imutáveis
#lanche[1] = 'Refigerante'
print(lanche[1])

print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba!')

for cont in range(0,len(lanche)):
    print(lanche[cont])

for cont in range(0, len(lanche)):
    print(f'{cont}ª eu vou comer {lanche[cont]}.')
print('Que delicia!')

for pos,comida in enumerate(lanche):
    print(f'{pos}ª eu vou comer {comida}.')
