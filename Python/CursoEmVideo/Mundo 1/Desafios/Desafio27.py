nome=str(input('Digite seu nome completo: ')).strip()
nome1=nome.split()
print('Prazer em te conhecer!')
print(f"Seu primeiro nome é {nome1[0].title()}.")
print(f"Seu último nome é {nome1[-1].title()}.")