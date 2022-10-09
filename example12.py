# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# ax**2 + b*x +c =0

a = -2
b = 2
c= 1
disc = b**2 - 4 * a * c # ищем дискриминант

if a==0:
    x= -c / b
    print(x)
elif disc >0:
    x1 = (-b - disc ** 0.5) / (2* a)
    x2 = (-b + disc ** 0.5) / (2* a)
    print(x1, x2)
elif not disc:
    x = -b / (2 * a)
    print(x)
else: print(" нет корней")


 

