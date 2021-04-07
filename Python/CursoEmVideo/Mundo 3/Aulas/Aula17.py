num = [5,9,3,4,6]
num[2] = 8

num.append(10)

num.sort(reverse=True)

num.insert(1,0)

num.pop()

num.remove(9)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4 na lista.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
