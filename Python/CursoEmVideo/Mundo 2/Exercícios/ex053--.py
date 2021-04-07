frase=str(input('Digite uma frase:')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso= junto[::-1]
#inverso=''      (Usando o for)
#for letra in range(len(junto) -1,-1,-1):
    #inverso += junto[letra]
print(f'O inverso de \033[33m{junto}\033[m é \033[32m{inverso}\033[m')
if inverso==junto:
    print('Temos um \033[34mPALÍNDROMO!\033[m')
else:
    print('A frase digitada \033[31mNÃO É UM PALÍNDROMO!\033[m')
