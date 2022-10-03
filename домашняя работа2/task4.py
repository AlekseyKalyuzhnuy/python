# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# выведите на экран их сумму.

number = input(" Введите число N")
result=dict()
for i in range (1,int(number)+1):

    result[i]=3+i+1
print(result)