s=0
count=0
for c in range(0,6):
    n=int(input('Digite um número:'))
    if n%2==0:
        s += n
        count += 1
print(f'Desconsiderando os números ímpares e somando os pares temos: {s}.')
