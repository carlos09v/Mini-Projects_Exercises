print('Vamos relembrar as unidades de medida!')
mdida=float(input('Uma distância em metros:'))
km=mdida/1000
hm=mdida/100
dam=mdida/10
dm=mdida*10
cm=mdida*100
mm=mdida*1000
print(f'{km}km\n{hm}hm\n{dam}dam\n{mdida:.1f}m\n{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm')
