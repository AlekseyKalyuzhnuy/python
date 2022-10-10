# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

n= int(input('Введите размер списка:'))
my_list=[]
for i in range(0, int(n)):
    elem=int(input('Введите число: '))
    my_list.append(elem)
print(my_list)  

my_list = list(set(my_list))
print(my_list)