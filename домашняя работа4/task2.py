#Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

num= int(input('Введите число: '))
result=[]
for i in range(1,10):
  if num % 2 ==0:
   elem=2 
   num= num/2
   result.append(elem)
  elif num % 3==0:
   elem=3
   num= num/3
   result.append(elem)
  elif num % 5==0:
   elem=5
   num= num/5
   result.append(elem)
  elif num % 7==0:
   elem=7
   num= num/7
   result.append(elem)
if num>1: 
  elem=int(num)
  result.append(elem)
print(result)



