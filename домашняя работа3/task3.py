#Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

n = int(input('Введите размер списка: '))
result=[]
for i in range(0, int (n)):
    elem=float(input('Введите число: '))
    result.append(elem)
print(result)

result2=[]
for i in range(0, int (n)):
    elem=round((result[i]-int(result[i])),5)
    result2.append(elem)
print(result2)

max=result2[0]
min=result2[0]
for i in range(0, int (n)):
    if result2[i]>max:
        max=result2[i]
    if result2[i]<min:
        min=result2[i]
print(max-min) 







