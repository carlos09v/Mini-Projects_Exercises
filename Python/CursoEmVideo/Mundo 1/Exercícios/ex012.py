print('Vamos ver quanto vale um produto com 5% de desconto.')
prod=float(input('Preço do produto: R$'))
desc=prod-prod*5/100
print(f'O produto que custava R${prod:.2f}, na promoção vai custar R${desc:.2f}.')