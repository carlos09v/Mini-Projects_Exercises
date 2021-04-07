casa=float(input('Qual o valor da casa: R$'))
salário=float(input('Salário do comprador: R$'))
anos=int(input('Quantos anos de financiamento?'))
min= salário*30/100
prestação= casa/(anos*12)
print(f'Para pagar uma casa de R$\033[32m{casa:.2f}\033[m em \033[34m{anos}\033[m anos,'
      f' a prestação será de R$\033[35m{prestação:.2f}\033[m')
if prestação<=min:
    print('Empréstimo pode ser \033[32mCONCEDIDO!\033[m')
else:
    print('Empréstimo \033[31mNEGADO!\033[m')
