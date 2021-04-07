from time import sleep
from playsound import playsound
print('Contagem regressiva para EXPLOSÃO:')
for c in range(10,0,-1):
    print(c)
    sleep(1)
print('\033[4:31mBUM!!BUMM!!! POOOW!! BOOM!\033[m')
playsound('Des46-fogos.mp3')
