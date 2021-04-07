soma = count = 0
while True:
    num= int(input('Digite um valor (999 para parar):'))
    if num ==999:
        break
    soma += num
    count += 1
print(f'Você digitou {count} valores e a soma entre eles foi {soma}.')
