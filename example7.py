# для натурального nсоздать словарь "индекс-значение", состоящее из  элементов последовательности 3n+1

n= input('Введите число n:')
result=[]
for i in range(1, int(n)+1):
    elem=[i,3*i+1]
    result.append(elem)
print(dict(result))  # dict- тип переменной для словаря


# образцовый вариант решения
number = input(" Введите число N")
result=dict()
for i in range (1,int(number)+1):

    result[i]=3+i+1
print(result)