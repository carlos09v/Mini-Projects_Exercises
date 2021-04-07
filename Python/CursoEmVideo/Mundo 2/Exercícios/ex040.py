n1=float(input('Primeira nota:'))
n2=float(input('Segunda nota:'))
m= (n1+n2)/2
print(f'Tirando {n1} e {n2}, a média do aluno é \033[34m{m}\033[m.')
if 7>m>=5:
    print('O aluno está em \033[33mRECUPERAÇÃO\033[m.')
elif m<5:
    print('O aluno está \033[31mREPROVADO\033[m.')
elif m>=7:
    print('o aluno está \033[32mAPROVADO\033[m.')
