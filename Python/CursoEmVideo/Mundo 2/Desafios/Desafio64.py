n1 = 0
count = 0
soma = 0
while n1 != 999:
    n1=int(input('Digite um número [999 to stop]:'))
    count += 1
    soma += n1
print('Finalmente acabou!')
print(f'Você digitou {count -1} números e a soma entre eles é {soma -999}.')
