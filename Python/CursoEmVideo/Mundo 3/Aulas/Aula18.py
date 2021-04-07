teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #Cópia
teste[0] = 'Pedro'
teste[1] = 18
galera.append(teste[:])
print(galera)

pessoal = [['Juca',22],['Maria',33],['Silvana',50]]
print(pessoal[1])
print(pessoal[0][1])
for p in pessoal:
    print(p)
for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos de idade.')
