def area(txt):
    print(txt)
    print('-'*20)
    larg=float(input('Largura (m): '))
    compri=float(input('Comprimento (m): '))
    are= larg*compri
    print(f'A área de um terreno {larg:.1f}x{compri:.1f} é de {are}m²')


area('Controle de Terrenos')
