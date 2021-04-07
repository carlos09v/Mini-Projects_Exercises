def escreva(txt,txt1,txt2):
    print('-='*len(txt))
    print(f'{txt:^20}')
    print('-='*len(txt))
    print('-=' * len(txt1))
    print(f'{txt1:^40}')
    print('-='*len(txt1))
    print('-=' * len(txt2))
    print(txt2)
    print('-='*len(txt2))


escreva('Olá,Mundo!','Opa, Baum? De Buenas?','Oi')
