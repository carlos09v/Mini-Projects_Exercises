def leiaInt(intei=0):
    while True:
        try:
            intei = int(input(intei))
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return intei

def leiaFloat(real=0):
    while True:
        try:
            real = float(input(real))
        except:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        else:
            return real


intei = leiaInt('Digite um Inteiro: ')
real = leiaFloat('Digite um Real: ')
