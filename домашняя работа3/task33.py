#Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

n = int(input('Введите размер списка: '))
result=[]
for i in range(0, int (n)):
    elem=float(input('Введите число: '))
    result.append(elem)
# print(result)

new_list = [round(i % 1 ,2) for i in result if i % 1 != 0]
print(new_list)
print(f'{result} => {max(new_list)-min(new_list)}')
