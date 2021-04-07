dados = dict()
lista = list()
total = 0
dados['nome']=str(input('Nome do jogador: ')).title()
n=int(input(f'Quantas partidas {dados["nome"]} jogou?' ))
for c in range(n):
    gols=lista.append(int(input(f'Quantos gols na partida {c}? ')))
    dados['gols']=lista[:]
    dados['total'] = sum(lista)
print('-='*30)
print(dados)
print('-='*30)
print(f'O campo nome tem o valor {dados["nome"]}.')
print(f'O campo gols tem o valor {dados["gols"]}.')
print(f'O campo total tem valor {dados["total"]}.')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {n} partidas.')
for c,v in enumerate(lista):
    print(f' => Na partida {c}, fez {v} gols.')
print(f'Foi um total de {dados["total"]}.')
