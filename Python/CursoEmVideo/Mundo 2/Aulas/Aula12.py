nome=str(input('Qual o seu nome:')).title().strip()
if nome=='Carlos':
    print('Que nome bonito!')
elif nome=='João' or nome=='Maria' or nome=='Enzo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Juliana Valeime Dolores':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem comum.')
print(f'Tenha um bom dia {nome}!')