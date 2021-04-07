from time import sleep
opção=0
n1=int(input('Primeiro valor:'))
n2=int(input('Segundo valor:'))
while opção!=5:
    print('''    \033[32m[\033[m \033[34m1\033[m \033[32m]\033[m \033[35msoma\033[m
    \033[32m[\033[m \033[34m2\033[m \033[32m]\033[m \033[35mmultiplicar\033[m
    \033[32m[\033[m \033[34m3\033[m \033[32m]\033[m \033[35mmaior\033[m
    \033[32m[\033[m \033[34m4\033[m \033[32m]\033[m \033[35mnovos números\033[m
    \033[32m[\033[m \033[34m5\033[m \033[32m]\033[m \033[35msair do programa\033[m''')
    opção=int(input('>>>> Qual a sua opção?'))
    if opção==1:
        soma= n1+n2
        print(f'A soma entre \033[32m{n1}\033[m e \033[32m{n2}\033[m é \033[33m{soma}\033[m.')
    elif opção==2:
        multiplica= n1*n2
        print(f'O resultado entre \033[32m{n1}\033[m x \033[32m{n2}\033[m é \033[34m{multiplica}\033[m.')
    elif opção==3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print(f'O maior entre \033[32m{n1}\033[m e \033[32m{n2}\033[m é \033[36m{maior}\033[m')
    elif opção==4:
        print('Informe os números novamente:')
        n1=int(input('Primeiro valor:'))
        n2=int(input('Segundo valor:'))
    elif opção==5:
        print('\033[31mFinalizando...\033[m'),sleep(3)
    else:
        print('\033[37mOpção inválida. Tente novamente!\033[m')
    print('-=-'*10)
print('\033[37mFim do programa. Volte sempre!\033[m')
