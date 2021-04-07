from random import randint
v = 0
while True:
    jogador=int(input('Diga um valor:'))
    pc = randint(0,10)
    total = jogador+pc
    tipo = ' '
    while tipo not in 'PIÍ':
        tipo=str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc}. Total de {total}.')
    print('Deu PAR.' if total%2==0 else 'Deu ÍMPAR.')
    if tipo=='P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I' or tipo == 'Í':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
