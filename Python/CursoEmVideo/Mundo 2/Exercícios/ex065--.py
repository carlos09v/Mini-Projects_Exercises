resp = 'S'
soma = media = quant = maior = menor = 0
while resp=='S':
    num=int(input('Digite um número:'))
    soma += num
    quant += 1
    if quant==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
    resp=str(input('Quer continuar? [S/N]')).upper().strip()[0]
media= soma/quant
print('Acabou!')
print(f'Você digitou {quant} números e média foi {media:.2f}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')
