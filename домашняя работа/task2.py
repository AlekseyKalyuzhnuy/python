#программа принимает на ввод координаты точки и выдает номер четвертти

x= int(input('Введите координаты по оси x : '))
y= int(input('Введите координаты по оси y : '))
if x>0 and y>0:
    print("1")
elif x<0 and y>0:
   print('2')
elif x<0 and y<0:
    print(('3'))
elif x>0 and y<0:
    print("4")
elif x==0 or y==0:
    print("введены некорректные данные ")
    

