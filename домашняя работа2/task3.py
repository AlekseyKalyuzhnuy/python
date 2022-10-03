#  задать список из N элементов, заполненный числами из промежутка [-N,N]. 
# Позиции хранятся в файле file.txt  в одной строке одно число
# Реализовать алгоритм смешения списка


import random
n=int(input('Введите число n:'))
result = []
for i in range(n):
  elem = random.randint(-n, n)
  result.append(elem)
print(result)

from random import shuffle
x = [i for i in result]
shuffle(x)
print(x)

data=open('file.txt', 'a')
data.write(str(result))
data.close()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

