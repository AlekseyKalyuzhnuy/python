# ввести число, программа должна выдать такое количество числе в случайном порядке

import random

n=int(input('Введите произвольное целое число: '))
for i in range(n):
    print(random.randint(-100,100), end=' ') #   выводит результаты в строку

