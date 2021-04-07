print('Vamos calcular o seu \033[32mIMC\033[m!')
alt=float(input('Qual a sua altura:'))
peso=float(input('Qual o seu peso:'))
imc= peso/(alt**2)
if imc<18.5:
    print(f'Seu IMC é {imc:.1f}. Você está \033[36mABAIXO DO PESO\033[m!')
elif imc>=18.5 and imc<25:
    print(f'Seu IMC é {imc:.1f}. Você está no \033[32mPESO IDEAL\033[m!')
elif imc>=25 and imc<30:
    print(f'Seu IMC é {imc:.1f}. Você está \033[33mSOBREPESO\033[m!')
elif imc>=30 and imc<=40:
    print(f'Seu IMC é {imc:.1f}. Você está com \033[37mOBESIDADE\033[m!')
else:
    print(f'Seu IMC é {imc:.1f}. Você está com \033[31mOBESIDADE MÓRBIDA\033[m!')
