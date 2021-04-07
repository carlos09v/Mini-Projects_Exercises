import math
print('Vamos ver um ângulo e ver seu seno,cosseno e tangente.')
an=float(input('Digite o ângulo que você deseja:'))
seno=math.sin(math.radians(an))
cos=math.cos(math.radians(an))
tan=math.tan(math.radians(an))
print(f'O ângulo de {an} tem o SENO de {seno:.2f}.\nO COSSENO de {cos:.2f}.\nA TANGENTE de {tan:.2f}.')