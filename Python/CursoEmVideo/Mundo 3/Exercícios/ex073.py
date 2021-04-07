times = ('Iternacional','São Paulo','Flamengo','Atlético-MG','Palmeiras','Grêmio','Fluminense','Ceará SC',
         'Santos','Corinthians','Bragantino','Atlético-PR','Atlético-GO','Sport Recife','Vasco da Gama',
         'Fortazela','Bahia','Goiás','Coritiba','Botafogo')
print(f'Brasileirão 2020: {times}')
print('-'*40)
print('Os 5 primeiros colocados:')
for c in range(1,6):
    print(f'{c}º {times[c-1]}')
print('-'*40)
print('Os 4 últimos colocados:')
print(times[-4:])
print('-'*40)
print('Em ordem alfabética:')
print(sorted(times))
print('-'*40)
print(f'O Corinthians está na {times.index("Corinthians")-1}ª posição.')
