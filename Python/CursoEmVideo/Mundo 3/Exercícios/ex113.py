def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('ERRO! Por favor, digite um número inteiro válido!')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('ERRO! Por favor, digite um número inteiro válido!')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

num = leiaInt('Digite um Inteiro: ')
numr = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {num} e o real {numr}.')
