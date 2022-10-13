#  Дан список чисел. Создать список, в который попадают числа,
# описываемые  возрастающую последовательность. 
# Порядок элементов менять нельзя
# Пример [1, 5, 2 , 3 , 4, 6, 1, 7]=>[1,2,3]

num = [4, 5, 2, 3, 4, 6, 1 ,7]
def nextmax(listt):
    max = listt[0]
    res= [listt[0]]
    for i in range(len(listt)):
        if listt[i] > max:
            max = listt[i]
            res.append(max)
    
    if len(res) ==1:
        res= nextmax(listt[1])
    return res

print(nextmax((num)))
