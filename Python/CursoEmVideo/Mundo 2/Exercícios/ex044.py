print(f'\033[33m{"=":=^40}\033[m')
print(f'\033[35m{" Lojas SoNoDally ":=^40}\033[m')
print(f'\033[33m{"=":=^40}\033[m')
preço=float(input('Preço das compras: \033[32mR$\033[m'))
print('''\033[34mFORMAS DE PAGAMENTO:\033[m
\033[31m[\033[m \033[32m1\033[m \033[31m]\033[m á vista dinheiro/cheque \033[4:36m(10% de desconto)\033[m
\033[31m[\033[m \033[32m2\033[m \033[31m]\033[m á vista cartão \033[4:36m(5% de desconto)\033[m
\033[31m[\033[m \033[32m3\033[m \033[31m]\033[m 2x no cartão
\033[31m[\033[m \033[32m4\033[m \033[31m]\033[m 3x ou mais no cartão \033[4:33m(20% de Juros)\033[m''')
opção=int(input('\033[35mQual é a opção?\033[m'))
if opção==1:
    total= preço-(preço*10/100)
elif opção==2:
    total= preço-(preço*5/100)
elif opção==3:
    total= preço
    parcela= preço/2
    print(f'Sua compra será parcelada em \033[32m2x\033[m de \033[4:33mR${parcela:.2f}\033[m \033[36mSEM JUROS\033[m')
elif opção==4:
    total= preço+(preço*20/100)
    totalparcelas= int(input('\033[36mQuantas parcelas?\033[m'))
    parcela= total/totalparcelas
    print(f'Sua compra será parcelada em \033[32m{totalparcelas}x\033[m de'
          f' \033[33mR$\033[m\033[33m{total:.2f}\033[m COM JUROS')
else:
    print('\033[31mOPÇÃO INVÁLIDA\033[m de pagamento. Tente novamente!')
print(f'Sua compra de \033[m\033[32mR${preço:.2f}\033[m vai'
      f' custar \033[4:33mR${total:.2f}\033[m no final.')
