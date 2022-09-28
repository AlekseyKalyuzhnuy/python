# для натурального nсоздать словарь "индекс-значение", состоящее из  элементов последовательности 3n+1

n= input('Введите число n:')
result=[]
for i in range(1, int(n)+1):
    elem=[i,3*i+1]
    result.append(elem)
print(dict(result))  # dict- тип переменной для словаря
