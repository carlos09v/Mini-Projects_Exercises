numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze',
           'quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n1=int(input('Digite um número entre 0 e 20:'))
    if 0 <= n1 <= 20:
        break
    print('Tente novamente! ',end='')
print(f'O número {n1} escrito por extenso é: {numeros[n1]}')
