lista=[]
for c in range(1,6):
    peso=float(input(f'Peso da {c}ª pessoa:'))
    lista += [peso]
print(f'O maior peso lido foi {max(lista)}Kg.')
print(f'O menor peso lido foi {min(lista)}Kg.')
