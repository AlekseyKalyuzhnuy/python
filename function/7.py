#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10 ]
new_list = []
for i in range(0, len(my_list)):
    if my_list.count(my_list[i])==1:  # ввели счетчик повторения элементов
        new_list.append(my_list[i])
print(new_list)


# второй вариант
#my_list = list(map(int,input("input list:").split()))

#list_unique = list(filter(lambda item: my_list.count(item) ==1, my_list))
print(list_unique)