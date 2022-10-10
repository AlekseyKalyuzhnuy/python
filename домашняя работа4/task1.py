#Вычислить число c заданной точностью d
# Пример:- при $d = 0.001, π = 3.141.$

from math import pi
d = float(input('Введите размер точности: '))
k=1
while d*(10**k)<1:
  k+=1
print(round(pi,k))

# второй вариант
#d=len(str(d).split('.')[1]) #  считаем, сколько символов после точки
#print(round(pi,d))