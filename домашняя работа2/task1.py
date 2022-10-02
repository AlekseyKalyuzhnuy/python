
num= float(input('Введите число: '))
num1=1
while num1 !=0:
  num=round(num*10,5)
  num1=num%10
num2=num//10
print(num2)

sum=0
while num2>0:
  sum=sum+num2%10
  num2=num2//10
print(sum)




 