#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний 


n= int(input('Введите размер списка:'))
result=[]
k=0
for i in range(0, int(n)):
    elem=int(input('Введите число: '))
    result.append(elem)
print(result)  
for i in range(0, int(n/2)):
   print(result[i]*result[n-1-i]) 
   
   





