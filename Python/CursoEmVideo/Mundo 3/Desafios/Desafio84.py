nome = []
povo = []
peso = []
pes = 0
while True:
    nome.append(str(input('Nome:')))
    nome.append(float(input('Peso:')))
    povo.append(nome[:])
    peso.append(nome[1])
    nome.clear()
    pes += 1
    print('Pessoa cadastrada com sucesso...')
    resp = ' '
    resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
    while resp not in 'S':
        print('Dado inválido! Tente novamente.')
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
print('-='*30)
print(f'Foram cadastradas {pes} pessoas')
print(f'As pessoas mais pesadas são: {max(peso)}Kg. Peso de ',end='')
for p in povo:
    if p[1]==max(peso):
        print(f'[{p[0]}] ',end='')
print(f'\nAs pessoas mais leves são: {min(peso)}Kg. Peso de ',end='')
for p in povo:
    if p[1]==min(peso):
        print(f'[{p[0]}] ',end='')
