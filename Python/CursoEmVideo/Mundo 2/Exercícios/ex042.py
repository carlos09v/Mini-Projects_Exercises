print('/_'*14)
print('Analisador de Triângulos v.2.0')
print('/_'*14)
seg1=int(input('Primeiro segmento:'))
seg2=int(input('Segundo segmento:'))
seg3=int(input('Terceiro segmento:'))
if seg1<seg2+seg3 and seg2<seg1+seg3 and seg3<seg2+seg1:
    print(f'Dados os segmentos {seg1} , {seg2} e {seg3}, é POSSÍVEL FORMAR um triângulo ', end='')
    if seg1==seg2==seg3:
        print('EQUILÁTERO!')
    elif seg1!=seg2!=seg3!=seg1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print(f'Dados os segmentos {seg1}, {seg2} e {seg3}, NÃO É POSSIVEL FORMAR um triângulo!')
