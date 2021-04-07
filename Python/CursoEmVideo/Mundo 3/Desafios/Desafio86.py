matriz = []
for c in range(0,9):
    matriz.append(int(input(f'Digite um valor para [{c}, {c+1}]: ')))
print('-='*30)
print(f'''
[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]
[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]
[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]''')
