print('-'*20)
print('Sequência de Fibonacci')
print('-'*20)
t1=0
t2=1
n = int(input('Quantos termos você quer mostrar?'))
print('~'*20)
print(f'{t1} - {t2}', end='')
count = 3
while count<=n:
    t3 = t1 + t2
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    count += 1
print(' - FIM!')
print('~'*20)
