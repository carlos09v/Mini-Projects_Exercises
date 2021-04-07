guys = list()
dado = list()
tormai = tormen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    guys.append(dado[:])
    dado.clear()
print(guys)
for p in guys:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
        tormai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        tormen += 1
print(f'Temos {tormai} pessoas maiores de idade nessa lista e'
      f' {tormen} menores de idade.')
