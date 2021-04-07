c = s = 0
num = 'Alinhamentos'
print(f'{num:-^40}')
print(f'{num:->40}')
print(f'{num:-<40}')
while True:
    n=int(input('Digite um número:'))
    if n==999:
        break
    c += 1
    s += n
print('Acabou!')
print(f'Você digitou {c} números e a soma entre eles é {s}!')
