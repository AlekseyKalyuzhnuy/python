# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
result=[]
n = int(input('Введите число для конвертации: '))
ost=n
for i in range(8):
    if n!=0:
     k = int( n/ 2)
     ost=n-k*2
     n= int (n/2)
     elem=ost
    else: break

    result.append(elem)   
ready = int(''.join(map(str,result)))
print(ready)


