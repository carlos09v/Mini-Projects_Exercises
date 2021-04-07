from time import sleep
sair= False
num1= int(input('Primeiro valor:'))
num2= int(input('Segundo valor:'))
while not sair:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção=int(input('>>>> Qual a sua opção?'))
    print('-=-'*10)
    if opção == 1:
        soma=num2+num1
        print(f'A soma entre {num1} e {num2} é {soma}.')
    elif opção == 2:
        multiplica=num2*num1
        print(f'O resultado entre {num1} x {num2} é {multiplica}.')
    elif opção == 3:
        if num2>num1:
            maior=num2
        else:
            maior=num1
        print(f'O maior número entre {num1} e {num2} é {maior}.')
    elif opção == 4:
        print('Informe novamente os valores!')
        num1=int(input('Primeiro valor:'))
        num2=int(input('Segundo valor:'))
    elif opção == 5:
       sair= True
       print('Finalizando...'),sleep(3)
    else:
        print('Opção inválida. Tente novamente!')
print('Fim do programa. Até mais!')
