'''
Erros: sintaxe -
Excenções: ZeroDivisionError ; ValueError ; NameError ; TypeError ; IndexError ; ModuleNotFoundError ...
'''
#Excessões
n = int(input('Digite um número: ')) # oito = ValueError
print(f'Você digitou o número {n}.')
print(x) # NameError
lista= [5,3,6]
print(lista[3]) # IndexError - Out of Range
import uteis # ModuleNotFoundError

# Tratamento de Erro
try:
    a = int(input('Numerador: '))
    b = int(input('Denomidador: '))
    d= a / b
except (ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'Infelizmente tivemos um problema :(')
    print(f'Problema encontrado foi: {erro.__class__}')
else:
    print(f'O resultado é {d:.1f}.')
finally:
    print('Volte sempre! Muito Obrigado!')
