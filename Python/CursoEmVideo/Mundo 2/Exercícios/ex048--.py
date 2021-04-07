print('\033[36mEx: Faça um programa que calcule a soma entre todos os números que são múltiplos'
      ' de três e que se encontram no intervalo de 1 até 500.\033[m')
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos \033[33m{cont}\033[m valores solicitados é \033[32m{soma}\033[m.')
