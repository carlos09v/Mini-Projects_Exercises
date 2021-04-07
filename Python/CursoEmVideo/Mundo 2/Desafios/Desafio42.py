from time import sleep
print('\033[33m/_\033[m'*14)
print('\033[35mAnalisador de Triângulos v.2.0\033[m')
print('\033[33m/_\033[m'*14)
seg1=int(input('Primeiro segmento:'))
seg2=int(input('Segundo segmento:'))
seg3=int(input('Terceiro segmento:'))
print('\033[31mAnalisando segmentos...\033[m')
sleep(2)
if seg1<seg2+seg3 and seg2<seg1+seg3 and seg3<seg2+seg1:
    print(f'Dados os segmentos \033[33m{seg1}\033[m , \033[33m{seg2}\033[m e \033[33m{seg3}\033[m,'
          f' é \033[32mPOSSÍVEL FORMAR\033[m um triângulo ', end='')
    if seg1==seg2==seg3:
        print('\033[33mEQUILÁTERO\033[m!')
    elif seg1!=seg2!=seg3!=seg1:
        print('\033[34mESCALENO\033[m!')
    else:
        print('\033[36mISÓSCELES\033[m!')
else:
    print(f'Dados os segmentos {seg1}, {seg2} e {seg3}, \033[31mNÃO É POSSIVEL FORMAR\033[m um triângulo!')
